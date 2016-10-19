# from igraph import *
# g = Graph(2)
# g.add_edges([('ankit','csv')])
# layout = g.layout("kk")
# plot(g, layout = layout)
from igraph import *
import csvtest
import matplotlib.pyplot as plt

# vertices = csvtest.get_countries()
edges = csvtest.get_year_data(2009)

g = Graph(edges=edges)
to_delete_ids = [v.index for v in g.vs if g.degree(v) == 0]
g.delete_vertices(to_delete_ids)
layout = g.layout("kk")
plot(g, layout = layout)

plt.plot(sorted(g.degree()))
plt.show()
