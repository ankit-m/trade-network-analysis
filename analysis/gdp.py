# GDP Analysis Explanation

import helpers
import csvreader
import matplotlib.pyplot as plt

def get_average_gdp(gdps):
    count = 0
    total = 0
    for i in gdps:
        if gdps[i] != '':
            total += float(gdps[i])
            count += 1
    return total/count

def assign_gdps(g, gdps):
    for v in g.vs():
        try:
            if gdps[str(v["label"])] == '':
                v["gdp"] = 0.0
            else:
                v["gdp"] = float(gdps[str(v["label"])])
        except KeyError:
            v["gdp"] = 0.0

def print_rich_nations(g, avg):
    print g.vs.select(gdp_gt=avg)["label"]

def find_percentage_trade_rich(g, avg, total):
    percentages = []
    rich_trade = 0;
    for v in g.vs():
        for i in g.neighbors(v.index, mode="out"):
            gdp = g.vs.select(i)['gdp'][0]
            if gdp > avg and v["gdp"] > avg:
                rich_trade += g.es.select(_source=v.index, _target=i)["weight"][0]
    return (rich_trade/total)*100

def trade_between_rich_poor(g, avg):
    rich_nations = []
    poor_nations = []
    c = 0
    for i in g.vs():
        if i['gdp'] > avg:
            rich_nations.append(c)
        else:
            poor_nations.append(c)
        c += 1
    ei = g.es.select(_source_in = rich_nations)
    ej = g.es.select(_target_in = poor_nations)
    co = 0.0
    for q in list(set(ei) & set(ej)):
        co += q['weight']
    a = g.es.select(_source_in = poor_nations)
    b = g.es.select(_target_in = rich_nations)
    ca = 0.0
    for p in list(set(a) & set(b)):
        ca += p['weight']
    return co/(co + ca)

def run():
    percentages = []
    trades_rp = []
    for year in range(1960, 2010):
        vertices = helpers.get_countries()
        edges, weights = csvreader.get_year_data(year, 1.0)
        g = helpers.create_connected_graph(vertices, edges, weights, True)
        gdps = csvreader.get_gdp(year)
        avg = get_average_gdp(gdps)
        total = sum(weights)
        assign_gdps(g, gdps)
        trades_rp.append(trade_between_rich_poor(g, avg))
        percentages.append(find_percentage_trade_rich(g, avg, total))
        print 'Processing year: %d' % year
    print "Average Trade Between Rich and Poor from 1960 - 2009: %f" % (sum(trades_rp)/len(trades_rp))
    plt.plot(range(1960, 2010), percentages)
    plt.xlabel('Year')
    plt.ylabel('Percentage of trade between rich nations')
    plt.show()
