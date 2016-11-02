# Is the world more connected over time?

import csvreader
import helpers
import matplotlib.pyplot as plt
from igraph import *

def plot():
    mean_degrees = []
    years = []
    vertices = helpers.get_countries()
    for i in range(1950, 2009):
        edges, weights = csvreader.get_year_data(i, 50.0)
        g = helpers.create_connected_graph(vertices, edges, weights, True)
        mean_degrees.append(mean(g.degree()))
        years.append(i)
        print 'Processing Mean Degree for year: %d' % i
    plt.plot(years, mean_degrees)
    plt.xlabel('Year')
    plt.ylabel('Mean Degree')
    plt.show()
