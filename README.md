## Low-Cost Carriers vs. Full Service Network Carriers in intra-European aviation

This repository contains the code accompanying my research on the differences between budget and mainline airlines within Europe from a complex network science perspective. It includes my network visualisations generated using [Gephi](https://gephi.org/) and relevant degree distribution plots.

This research used datasets from [EUROCONTROL's Aviation Data Repository for Research](https://www.eurocontrol.int/dashboard/aviation-data-research) which cannot be shared publicly. The network files have therefore been omitted also. A .pdf describing the corresponding data's structure can be found at the above link. 

The list of airport ICAO codes was provided by [openflights.org](https://openflights.org/data.php)

### Abstract
The Low-Cost Carrier (LCC) airline model has become well-established in the European airspace since they joined the market in the early 2000s. Contrary to the traditional hub-and-spoke topology adopted by Full Service Network Carriers (FSNC), LCCs operate a point-to-point model and alternative business practices that minimises operational costs and allow them to provide substantially cheaper tickets than FSNCs. I interpret the structural properties of the intra-European commercial passenger aviation network from 2015 to 2019. Comparing the structural properties of the network of LCC and FSNC routes, I find that the alternative topologies corresponding to these competing market segments display multiple key characteristics indicative of their use of hubs and ’focus cities’. By analysing LCC network growth over this time period, I present insight into the flexibility of the point-to-point model with implications for future study of LCC expansion.

### Key Research Questions
1. What are the properties of the intra-European commercial passenger aviation network?
2. How has the commercial aviation network evolved over the period of 2015-2019?
3. How do the route networks of European LCCs and FSNCs differ from one another? Can we
identify key distinguishing properties that are indicative of their respective topologies?
4. Has the European LCC network demonstrated growth relative to its increase in market share
from 2015-2019?

### Findings
Consistent with prior literature on the global aviation network, the intra-European commercial aviation network exhibits signs of a heavy-tailed power-law degree distribution. I also find that the network shows signs of steady growth through node and edge expansion without undergoing any notable structural changes from 2015-2019. I identify multiple network properties that distinguish the LCC and FSNC networks and link back to the topologies on which their business models rely. The strongest indicators are the distribution of connections provided by each airport (unweighted-degree distribution) and the betweenness-centrality concentrations. I also observe deviations in mixing pattern and centrality concentration from the joint network that support the existence of ’focus cities’ within LCC networks, airports that act as bases for LCCs to operate from without returning to as often as FSNCs do to their hubs.
