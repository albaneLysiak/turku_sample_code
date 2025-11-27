# turku_sample_code
SpecOMS is a software creating an output file from 1) a set of experimental mass spectra to identify 2) a protein library.
The output is under the form "mass spectrum identifyer / best candidate peptide / shared peaks count / shared peaks count after realignement".
Several best candidates can be affected to one spectrum.

During my PhD, the aim was to evaluate several strategies to select the best peptide candidate / the best set of candidates for one spectrum. To do so, I took a step back and evaluated several ways to do so using
- the SpecOMS software, allowing to perform this search with several strategies
- theoretical spectra instead of experimental spectra; their sequences are known, which allows to evaluate the results with precision

This Python script taking as input data provided by SpecOMS and creating
1) a .gexf network from these data, that can be visualised graphically, for example by Gephi (not possible with the whole network)
2) statistics and histogram for the network (not really relevant for a reduced network)
This allowed me to perform a first exploration of the results provided by SpecOMS with the human proteome.

Main steps :

1) cleans the result file to have a smaller set of origins annotations (target / decoy)
2) creates a network between two peptides with a threshold of origin as well as shared peaks count, which allows to have a smaller network, that can thus be visualized (comment to have the histogram for the whole network)
Steps 3 and 4 must be executed if the .gexf is wanted, not if you want the complete network and the histogram
4) cleans the network to remove isolated nodes and those who have more than 5 neighbours
5) Saves the network as a .gexf file, that can be open for example by Gephi (see last part for a quick tutorial)

Steps 6, 7 and 8 must be executed if to analyse and visualise the histogram of the complete network
7) Computation of the number of nodes and edges of the network
8) Computation of the average degree for target, decoy nodes as well as all the nodes
9) Visualisation of the connectivity in the network under the form of a histogram

================================================================================

How to visualize properly the network with Gephi ?
1) Open network.gexf with Gephi
2) Go to partition (left panel) -> choose "origin" as attribute -> apply
3) Layout -> Fruchterman Reingold -> Run
A few minutes later, the spatialisation algorithm did its job.

This work allowed to see, in a theoretical context, a link between structures in the network and quality if the identifications.

