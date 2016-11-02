import helpers
import csvreader
from igraph import *
import numpy as np
import matplotlib.pyplot as plt

# jaccard + percentage trade + avg degree
def jaccard (a, b):
    if len(list(set(a) | set(b))) != 0:
        return len(list(set(a) & set(b)))/float(len(list(set(a) | set(b))))
    return 0.0

def percentage_trade (g, i, j):
    tot_bt = sum(g.es.select(_between = ([i], [j]))['weight'])
    tot_source = sum(g.es.select(_source_in = [i, j])['weight'])
    tot_target = sum(g.es.select(_target_in = [i, j])['weight'])
    return float(tot_bt/(tot_target + tot_source - tot_bt))

def avg_degree (g, i, j):
    return float(g.vs()[i].degree() + g.vs()[j].degree())/(2*g.vcount())

def ally_score (x, y, z):
    return float(x + y + z)/3

def run():
    vertices = helpers.get_countries()
    edges, weights = csvreader.get_year_data(2009, 5000.0)
    g = helpers.create_connected_graph(vertices, edges, weights, True)
    scores = []
    countries = []
    for i in range(g.vcount()):
        scores.append([])
        countries.append(g.vs()[i]['label'])
        for j in range(g.vcount()):
            if i != j:
                a = g.vs()[i].neighbors(mode=OUT)
                b = g.vs()[j].neighbors(mode=OUT)
                jac = jaccard(a, b)
                avd = avg_degree(g, i, j)
                per = percentage_trade(g, i, j)
                scores[i].append(ally_score(jac, avd, per))
            else:
                scores[i].append(0.0)
    plt.imshow(scores, cmap=plt.cm.Spectral_r, interpolation='nearest')
    plt.colorbar()
    # plt.xticks(range(len(scores)), countries, fontsize=4, rotation='vertical')
    plt.show()
