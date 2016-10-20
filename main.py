from igraph import *
import matplotlib.pyplot as plt
import csvreader
import helpers

vertices = helpers.get_countries()
edges = csvreader.get_year_data(2009)

g = Graph(vertex_attrs={"label": vertices}, edges=edges)
g.vs["name"] = vertices
to_delete_ids = [v.index for v in g.vs if g.degree(v) == 0]
g.delete_vertices(to_delete_ids)

layout = g.layout("kk")
plot(g, layout = layout)

# plt.plot(sorted(g.degree()))
# plt.show()
