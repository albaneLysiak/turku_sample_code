import networkx as nx
import collections
import matplotlib.pyplot as plt
import statistics
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.axis import Axis

#================ Creation of the network from SpecOMS data ================

specOMS_output = "specOMS_shift_all_solutions.csv"

G = nx.Graph() #the network is created

origins = {}
names = {}
ori = []

with open(specOMS_output, "r") as input_file :
    input_file.readline()
    i = 0
    for line in input_file :
        i += 1
        line = line.split(";")
        pep1 = line[0]
        pep2 = line[1]
        or1 = line[10].replace("\n", "")
        or1 = or1.replace("Contaminant and Target","Target")
        or1 = or1.replace("Contaminant","Target")
        or2 = line[9]
        or2 = or2.replace("Contaminant and Target","Target")
        or2 = or2.replace("Contaminant","Target")
        or2 = or2.replace("Multiple","Decoy")
        spc = float(line[2])
        #if or1 != "Decoy" and or1 != "Multiple" : #whole network version
        if or1 != "Decoy" and or1 != "Multiple" and spc >= 10 : #reduced network version
            G.add_edge(pep1,pep2)
            origins[pep1] = or1
            origins[pep2] = or2
            ori.append(or1)
            ori.append(or2)

nx.set_node_attributes(G, origins, "origin")

#comment the following 6 lines if complete network version

for node in list(G.nodes) :
    if G.degree[node] < 5 :
        G.remove_node(node)
for node in list(G.nodes) :
    if G.degree[node] == 0 :
        G.remove_node(node)

#The network is saved as a gephi readable file
nx.write_gexf(G, "network.gexf")

print("The network is saved")

#================ Statistics of the network ================

print(G.number_of_nodes())
print(G.number_of_edges())

degrees = []
degrees_t = []
degrees_d = []

for node in G.nodes() :
    degrees.append(G.degree(node))
    if origins[str(node)] ==  "Target" :
        degrees_t.append(G.degree(node))
    elif origins[str(node)] ==  "Decoy" :
        degrees_d.append(G.degree(node))

print("Average of degrees")
print(round(statistics.mean(degrees),2))
print("Average of degrees of target nodes")
print(round(statistics.mean(degrees_t),2))
print("Average of degrees of decoy nodes")
print(round(statistics.mean(degrees_d),2))

#================ Visualisation of the network as a histogram of degrees ================

fig = plt.figure(figsize=(16,6))

b2 = [i for i in range(1,146,5)]
b = [i for i in range(1,146)]
b[0] = 1
b2[0] = 1
n, bins, patches = plt.hist(degrees, bins = b)
plt.xticks(b)

ax = plt.gca()
locator = MultipleLocator(5)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(MultipleLocator(1))

plt.xlim(left = 0, right = 144)

plt.yscale('log')

plt.ylabel("Distribution of degrees of nodes in the peptides network")
plt.ylabel("Number of nodes")
plt.xlabel("Degree")

#grid
facecolor = '#EAEAEA'
color_bars = '#3475D0'
plt.grid(axis='y', color=color_bars, lw = 0.5, alpha=0.7)
plt.grid(color='white', lw = 0.5, axis='x', which = 'both')

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300


plt.show()
