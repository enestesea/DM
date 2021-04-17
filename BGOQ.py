import networkx as nx
from networkx.algorithms.tree import mst
from igraph import *
#prufer
g = Graph()
f = open("graphV.txt", "r")
for i in f.read().split("\n"):
    g.add_vertex(i)
f.close()
f = open("spanning.txt", "r")
for i in f.read().split("\n"):
    i = i.split(" ")
    g.add_edge(i[0], i[1])
for i in range(len(g.vs)):
    print(i,":", g.vs[i]["name"], end=", ")
print(g.to_prufer());

# L связный граф
fin = open('congraph.txt', 'r')
mas = [[0] * 3 for i in range(82)]
for i in range(82):
    s = fin.readline()
    k = s.split()
    for j in range(2):
        mas[i][j] = k[j]
L = nx.Graph()
L.add_weighted_edges_from(mas)

#веса связного графа
fin = open('graphsv.txt', 'r')
mas = [[0] * 3 for i in range(82)]
for i in range(82):
    s = fin.readline()
    k = s.split()
    for j in range(2):
        mas[i][j] = k[j]
    mas[i][2] = int(k[2])
G = nx.Graph()
G.add_weighted_edges_from(mas)
#b
print("rad(G) = ", nx.radius(G), ", diam(G) = ", nx.diameter(G), ", girth(G) = ", len(min(nx.cycle_basis(G))), ", center(G) = ", nx.center(G), ", k_node_connectivity = ", nx.node_connectivity(G), ", k_edge_connectivity = ", nx.edge_connectivity(G))
print()

#maxmatching g
print("M =", nx.max_weight_matching(L))
print()


#mst о
MST=nx.Graph(mst.minimum_spanning_tree(G))
print("MST = ", MST.edges)
print("MST =", sum(c for (a,b,c) in (MST.edges.data('weight'))))
print()
