import csv
import json
import networkx as nx
codefile = open('data/codes.csv' , 'r')
disputefile = open('data/MID.csv','r')
codefile.readline()
disputefile.readline()
disputes =  ['4401', '4407', '4408', '4414', '4436', '4483', '4488', '4491', '4492', '4493', '4507', '4508', '4545', '4547', '4548', '4575', '4585', '4588', '4593', '4598', '4599']
def getCodes():
    codes = {}
    reader = csv.reader(codefile , delimiter = ',')
    for row in reader:
        codes.update({row[1] : row[2]})
    return codes

def getEdges():
    codes = getCodes()
    Edges = [[] for i in range(0 , len(disputes))]
    reader = csv.reader(disputefile , delimiter = ',')
    prev = disputes[0]
    i=0
    for row in reader:
        if row[0] in disputes:
            if row[0] == prev:
                Edges[i].append(codes[row[3]])
            else:
                prev = row[0]
                i = i+1
                Edges[i].append(codes[row[3]])
    return Edges




G = nx.Graph()
Edgelist = getEdges()
print Edgelist

for i in range(0 , len(Edgelist)):
    G.add_edge(Edgelist[i][0] , Edgelist[i][1])


nx.write_gml(G , 'dispute.gml')
