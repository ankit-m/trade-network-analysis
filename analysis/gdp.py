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
    print 'Total: ', count, 'Avg: ', total/count
    return total/count

def assign_gdps(g, gdps):
    for v in g.vs():
        try:
            if gdps[str(v["name"])] == '':
                v.delete()
            else:
                v["gdp"] = float(gdps[str(v["name"])])
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
            if gdp < avg and v["gdp"] < avg:
                rich_trade += g.es.select(_source=v.index, _target=i)["weight"][0]
    percentages.append((rich_trade/total)*100)
    return percentages

def run():
    for year in range(1960, 2010):
        vertices = helpers.get_countries()
        edges, weights = csvreader.get_year_data(year, 500.0)
        g = helpers.create_connected_graph(vertices, edges, weights, True)
        gdps = csvreader.get_gdp(year)
        avg = get_average_gdp(gdps)
        total = sum(weights)
        assign_gdps(g, gdps)
        percentages = find_percentage_trade_rich(g, avg, total)
        print 'Processing year: %d/%d' % (year, 2008)

    plt.plot(range(1960, 2010), percentages)
    plt.xlabel('Year')
    plt.ylabel('Percentage of trade between rich nations')
    plt.show()
