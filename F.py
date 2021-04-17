from igraph import *
g = Graph()
f = open("vertex.txt", "r")
for i in f.read().split("\n"):
    g.add_vertex(i)
f.close()
f = open("graph.txt", "r")
for i in f.read().split("\n"):
    i = i.split(" ")
    g.add_edge(i[0], i[1])
for i in g.largest_independent_vertex_sets()[0]:
    print(g.vs[i]["name"], end=" ")
