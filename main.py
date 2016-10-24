from igraph import *
import matplotlib.pyplot as plt
import csvreader
import helpers

vertices = helpers.get_countries()
edges, weights = csvreader.get_year_data(2009, 10000.0)

g = Graph(vertex_attrs={"label": vertices}, edges=edges, directed=True)
g.vs["name"] = vertices
g.es["weight"] = weights

to_delete_ids = [v.index for v in g.vs if g.degree(v) == 0]
g.delete_vertices(to_delete_ids)

# print g.degree_distribution(bin_width = 1)
print "Network Diameter: %d" % g.diameter()
print "Largest Clique Size: %d" % g.omega()
# plt.plot(g.closeness(vertices=None, mode=ALL, cutoff=None, weights=None, normalized=True))
# plt.show()

print g.degree()
layout = g.layout("fr")
plot(g, layout = layout)

# plt.hist(g.degree())
# plt.show()
