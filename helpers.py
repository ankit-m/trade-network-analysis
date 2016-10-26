import json
from igraph import *

def initialize_data():
    countries = {};
    count = 0
    reader = csv.reader(csvfile, delimiter=',')
    csvfile.readline()
    for row in reader:
        if row[3] not in countries and row[3] != "":
            countries[row[3]] = count
            codes.append(row[3])
            count += 1
    with open('data/countries.json', 'w') as fp:
        json.dump(countries, fp, sort_keys=True, indent=4)
    with open('data/codes.json', 'w') as fp:
        json.dump(codes, fp, sort_keys=True, indent=4)

def get_countries():
    codes = open('data/codes.json', 'r')
    code = json.load(codes)
    return code

def get_codes():
    c = open('data/countries.json', 'r')
    co = json.load(c)
    return co

def create_connected_graph(vertices, edges, weights, d):
    g = Graph(vertex_attrs={"label": vertices}, edges=edges, directed=True)
    g.vs["name"] = vertices
    g.es["weight"] = weights
    to_delete_ids = [v.index for v in g.vs if g.degree(v) == 0]
    g.delete_vertices(to_delete_ids)
    return g
