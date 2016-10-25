from igraph import *
from analysis import *
import matplotlib.pyplot as plt
import csvreader
import helpers

degree.plot()

# vertices = helpers.get_countries()
# edges, weights = csvreader.get_year_data(2009, 10000.0)
# g = helpers.create_connected_graph(vertices, edges, weights, True)
#
# # print g.degree_distribution(bin_width = 1)
# print "Network Diameter: %d" % g.diameter()
# print "Largest Clique Size: %d" % g.omega()
# print "Reciprocity: %d" % g.reciprocity(mode="ratio")
# print "Mean Degree: %d" % mean(g.degree())
#
# # g.write_gml('test.gml')
# # plt.plot(g.closeness(vertices=None, mode=ALL, cutoff=None, weights=None, normalized=True))
# # plt.show()
#
# layout = g.layout("fr")
# plot(g, layout = layout)
