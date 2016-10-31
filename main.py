from igraph import *
from analysis import *
import matplotlib.pyplot as plt
import csvreader
import helpers

# degree.plot()
vertices = helpers.get_countries()
edges, weights = csvreader.get_year_data(2009, 5000.0)
g = helpers.create_connected_graph(vertices, edges, weights, True)

print "Network Diameter: %d" % g.diameter()
print "Largest Clique Size: %d" % g.omega()
print "Reciprocity: %d" % g.reciprocity(mode="ratio")
print "Mean Degree: %d" % mean(g.degree())
# for i in g.vs():
#     print i['name'], i.betweenness(), i.closeness()
# print g.betweenness()
# print g.closeness()
gdp.run()
# deletion.run(g)

# g.write_gml('world_trade.gml')
# layout = g.layout("fr")
# plot(g, layout = layout)
