import networkx as nx
import os
import csv

LCC = {'RYR', 'RUK', 'EZY', 'EJU', 'WAZ', 'WZZ', 'WMT', 'WUK'}
FSNC = {'THY', 'TRK', 'DLH', 'LHX', 'CLH', 'AFR'}

# To generate the LCC or FSNC networks, set one value to True 
# To generate the general network, set both to False
FILTER_LCC = False
FILTER_FSNC = False

europe_countries = [
    "Albania",
    "Andorra",
    "Armenia",
    "Austria",
    "Belarus",
    "Belgium",
    "Bosnia and Herzegovina",
    "Bulgaria",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Faroe Islands",
    "Finland",
    "Åland Islands",
    "France",
    "Georgia",
    "Germany",
    "Gibraltar",
    "Greece",
    "Holy See (Vatican City)",
    "Hungary",
    "Iceland",
    "Ireland",
    "Italy",
    "Kazakhstan",
    "Latvia",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Monaco",
    "Moldova",
    "Montenegro",
    "Netherlands",
    "Norway",
    "Poland",
    "Portugal",
    "Romania",
    "Russia",
    "San Marino",
    "Serbia",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Svalbard and Jan Mayen Islands",
    "Sweden",
    "Switzerland",
    "Turkey",
    "Ukraine",
    "North Macedonia",
    "United Kingdom",
    "Guernsey",
    "Jersey",
    "Isle of Man",
]

# Get the list of all files and directories
path = ".//Dataset"
yearList = os.listdir(path)

# Maps ICAO code to a dict holding IATA, latitude, longitude, country 
ICAOairports = dict()

with open('ICAO_airports.csv', newline='', encoding='utf-8-sig') as csvfile:
    airportData = csv.DictReader(csvfile, delimiter=',')
    for row in airportData:
        ICAOairports[row['ICAO']] = dict(IATA=row['IATA'], name=row['name'], country=row['country'], latitude=row['latitude'], longitude=row['longitude'])

for year in yearList:
    if FILTER_FSNC and FILTER_LCC:
        print("Cannot filter for FSNC and LCC at once.")
        break

    print("Building network for:", year)

    file_list = os.listdir(path +"//"+year)
    G = nx.MultiDiGraph()

    for file in file_list:
        with open(path +"//"+year+"//"+file, newline='', encoding='utf-8-sig') as flightFile:
            dataReader = csv.DictReader(flightFile, delimiter=',')
            for flight in dataReader:
                
                # Skip non-scheduled flights 
                if flight['ICAO Flight Type'] == 'N': continue

                # Skip flights w/out market segment 'Traditional Scheduled' or 'Lowcost'
                if flight['STATFOR Market Segment'] not in ['Traditional Scheduled', 'Lowcost']: continue

                DEST = flight['ADES']    
                DEPART = flight['ADEP']

                # Skip flights returning to the same DESTNATIONtination
                if DEPART == DEST: continue

                # Skip flights departing/arriving at airports without an ICAO code 
                if DEPART == 'ZZZZ' or DEST == 'ZZZZ': continue

                if (ICAOairports.get(DEPART) and ICAOairports.get(DEST)):
                    # Skip flights with non-European destinations 
                    if ICAOairports.get(DEPART).get('country') not in europe_countries: continue
                    
                    # Skip flights with non-European origins 
                    if ICAOairports.get(DEST).get('country') not in europe_countries: continue
                    
                    # Filter to only include flights from the top 3 LCCs
                    if FILTER_LCC and flight['AC Operator'] not in LCC: continue
                    
                    # Filter to only include flights from the top 3 FSNCs
                    if FILTER_FSNC and flight['AC Operator'] not in FSNC: continue 


                # Add a new airport node if needed and if airport exists in ICAO index 

                if DEPART not in G:
                    attr = ICAOairports.get(DEPART)
                    if attr: G.add_node(DEPART, IATA=attr.get('IATA') ,name=attr.get('name'), latitude=float(attr.get('latitude')), longitude=float(attr.get('longitude'))) 
                    else: 
                        #print("match not found for ICAO:", DEP)
                        continue

                if DEST not in G:
                    attr = ICAOairports.get(DEST)
                    if attr: G.add_node(DEST, IATA=attr.get('IATA') ,name=attr.get('name'), latitude=float(attr.get('latitude')), longitude=float(attr.get('longitude'))) 
                    else: 
                        #print("match not found for ICAO:", DES)
                        continue
                
                G.add_edge(DEPART, DEST, weight=1)

    # Convert to pure directed graph and sum weights across parallel edges 
    directed = nx.DiGraph()

    for node, attrs in G.nodes(data=True):
        directed.add_node(node, **attrs)

    for u, v, data in G.edges(data=True):
        w = data.get("weight", 1)
        if directed.has_edge(u, v):
            directed[u][v]["weight"] += w
        else:
            directed.add_edge(u, v, weight=w)

    # Remove nodes with degree < 1
    for node in list(directed.nodes):
        if directed.degree[node] < 1: directed.remove_node(node)
                
    # Save to .graphml format
    if FILTER_LCC:
        with open("LCC"+year+".graphml", "wb") as f:
            nx.readwrite.write_graphml(directed, f)

    elif FILTER_FSNC:
        with open("FSNC"+year+".graphml", "wb") as f:
            nx.readwrite.write_graphml(directed, f)

    else:
        with open("JOINT"+year+".graphml", "wb") as f:
            nx.readwrite.write_graphml(directed, f)




