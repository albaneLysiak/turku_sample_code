# turku_sample_code
SpecOMS is a software creating an output file from 1) a set of experimental mass spectra to identify 2) a protein library.
The output is under the form "mass spectrum identifyer / best candidate peptide / shared peaks count / shared peaks count after realignement".
Several best candidates can be affected to one spectrum.

During my PhD, the aim was to evaluate several strategies to select the best peptide candidate / the best set of candidates for one spectrum. To do so, I took a step back and evaluated several ways to do so using
- the SpecOMS software, allowing to perform this search with several strategies
- theoretical spectra instead of experimental spectra; their sequences are known, which allows to evaluate the results with precision

This Python script taking as input data output data provided by SpecOMS (available at https://mega.nz/file/HVMVBIgQ#8LmaWRo1WRsZNYZM30iNb85HzpCXOSwU0BUPSh74JZI) and creating
1) a .gexf network from these data, that can be visualised graphically, for example by Gephi ; to do such a visualisation, the data has to be reduced
2) statistics and histogram for the complete network
This work allowed me to perform a first exploration of the results provided by SpecOMS with the human proteome

Main steps :

1) cleans the result file to have a smaller set of origins annotations (target / decoy, see explanation NB at the end of readme)
2) creates a network between two peptides with a threshold of origin as well as shared peaks count, which allows to have a smaller network, that can thus be visualized (comment to have the histogram for the whole network) using the networkx package
Steps 3 and 4 must be executed if the .gexf is wanted, not if you want the complete network and the histogram
3) cleans the network to remove isolated nodes and those who have more than 5 neighbours
4) Saves the network as a .gexf file, that can be open for example by Gephi (see end of readme for a quick tutorial)

Steps 5, 6 and 7 must be executed if to analyse and visualise the histogram of the complete network

5) Computation of the number of nodes and edges of the network
6) Computation of the average degree for target, decoy nodes as well as all the nodes
7) Visualisation of the connectivity in the network under the form of a histogram
This histogram allowed me to see that, like many biological networks, this one had scale-free characteristics, with many nodes having a few neighbours, and a few nodes (hubs) with a high degree.

================================================================================

How to visualise properly the network with Gephi ?
1) Open network.gexf with Gephi
2) Go to partition (left panel) -> choose "origin" as attribute -> apply
3) Layout -> Fruchterman Reingold -> Run
A few minutes later, the spatialisation algorithm did its job, and the network can be visualise. We can guess a link between the density of parts of the network, and quality of identifications, because most of decoy nodes are in lower density areas.
See "network.gephi" to see the complete spatialised network.

NB : during the step of identification, the target / decoy strategie is often used. Decoy nodes are created, for example by reversing the peptides sequences. These decoy peptides are then considered as false positive identifications, and the score threshold is increaed up to a value allowing to have a given proportion of decoy peptides (generally, 1%). We then consider that target peptides have a similar value of FP rate. This is why, in the network, I consider decoy peptides as "low quality" peptides.

This work allowed to see, in a theoretical context, a link between structures in the network and quality of the identifications.

