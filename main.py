from igraph import *
from analysis import *
import matplotlib.pyplot as plt
import csvreader
import helpers
import json
from dispute_network import reader


#degree.plot()
def adddisputes(g , disputes):
    for i in range(0 , len(disputes)):
        if disputes[i][0] in g.vs["name"] and disputes[i][1] in g.vs["name"]:
            g.add_edge(disputes[i][0] , disputes[i][1] , weight = -1)
            g.add_edge(disputes[i][1] , disputes[i][0] , weight = -1)



vertices = helpers.get_countries()
edges, weights = csvreader.get_year_data(2000, 500.0)
g = helpers.create_connected_graph(vertices, edges, weights, True)

#print json.dumps(g.vs["name"], indent=4 ,sort_keys=True)
disputes = reader.getEdges()
adddisputes(g , disputes)



# print g.degree_distribution(bin_width = 1)
#print "Network Diameter: %d" % g.diameter()
#print "Largest Clique Size: %d" % g.omega()
#print "Reciprocity: %d" % g.reciprocity(mode="ratio")
#print "Mean Degree: %d" % mean(g.degree())
# for i in g.vs():
#     print i['name'], i.betweenness(), i.closeness()
# print g.betweenness()
# print g.closeness()

# print g.neighbors(0, mode="out")
# print g.es.select(_source=0, _target=1)["weight"]


g.write_gml('world_trade.gml')
# layout = g.layout("fr")
# plot(g, layout = layout)
