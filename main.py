from igraph import *
from analysis import *
import matplotlib.pyplot as plt
import csvreader
import helpers
import pandas as pd

YEAR = 2009
THRESHOLD = 5000.0

vertices = helpers.get_countries()
edges, weights = csvreader.get_year_data(YEAR, THRESHOLD)
g = helpers.create_connected_graph(vertices, edges, weights, True)

print '***********************************************'
print 'Plot Network'
print '***********************************************'

layout = g.layout("fr")
plot(g, layout = layout)

print '***********************************************'
print 'Network Statistics'
print '***********************************************'

print "Network Diameter: %f" % g.diameter()
print "Largest Clique Size: %d" % g.omega()
print "Reciprocity: %f" % g.reciprocity(mode="ratio")
print "Mean Degree: %f" % mean(g.degree())
print "Average Path Length %f" % g.average_path_length(directed=True)
print "Clustering Coefficient %f" % g.transitivity_undirected()

fig = plt.figure()

ax1 = fig.add_subplot(221)
sc = pd.Series(g.closeness())
sc.plot.bar(color = 'white', edgecolor='0.35', width=1.0)
ax1.set_ylim([0.3, 0.8])
ax1.set_ylabel('Closeness')
ax1.axes.get_xaxis().set_ticks([])

ax2 = fig.add_subplot(222)
sb = pd.Series(g.betweenness())
sb.plot.bar(color = 'white', edgecolor='0.35', width=1.0)
ax2.set_ylabel('Betweenness')
ax2.axes.get_xaxis().set_ticks([])

ax3 = fig.add_subplot(223)
sd = pd.Series(g.degree())
sd.hist(color = 'white', edgecolor='0.35', bins=10)
ax3.set_ylabel('Frequency')
ax3.set_xlabel('Degree')

ax3 = fig.add_subplot(224)
sa = pd.Series(g.authority_score(weights='weight', scale=True, return_eigenvalue=False))
sh = pd.Series(g.hub_score(weights='weight', scale=True, return_eigenvalue=False))
sa.plot.bar(color = '0.35', edgecolor='0.35', width=0.4, position=0)
sh.plot.bar(color = 'red', edgecolor='red', width=0.4, position=1)
ax3.set_ylabel('Hub and Authority Score')
ax3.legend(('Authority', 'Hub'))
ax3.axes.get_xaxis().set_ticks([])
ax3.set_xlabel('Countries')

plt.show()

print '***********************************************'
print 'Network Analysis'
print '***********************************************'

print '-> Degree Analysis'
degree.plot()

print '-> GDP Analysis'
gdp.run()

print '-> Node Deletion'
deletion.run(g)

print '-> Country Alliance'
allies.run()

# g.write_gml('world_trade.gml')
