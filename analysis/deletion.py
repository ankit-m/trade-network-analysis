import random
from igraph import *
import copy
import matplotlib.pyplot as plt

def get_sorted_vs (g):
    seq = g.closeness()
    ids = [i[0] for i in sorted(enumerate(seq), key=lambda x:x[1])]
    return list(reversed(ids))

def run (g):
    c = get_sorted_vs(g)
    means = []
    countries = []
    for i in range(30):
        print 'Deleting: ',c[i] , ' ', g.vs()[c[i]]['label']
        edges = g.es.select(_source_eq = c[i])
        g.delete_edges(edges)
        edges = g.es.select(_target_eq = c[i])
        g.delete_edges(edges)
        means.append(mean(g.degree()))
        countries.append(str(g.vs()[c[i]]['label']))
        # plot_graph(g)
    plt.plot(means)
    plt.xticks(range(len(means)), countries, size='small', rotation='vertical')
    plt.show()

def plot_graph (g):
    temp = copy.deepcopy(g)
    to_delete_ids = [v.index for v in temp.vs if temp.degree(v) == 0]
    temp.delete_vertices(to_delete_ids)
    layout = temp.layout("fr")
    plot(temp, layout = layout)
