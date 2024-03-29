# rows
# 2 : year
# 3 : country 1
# 4 : country 2
# 5 : 1 -> 2
# 6 : 2 -> 1
import csv
import json

csvfile = open('data/data.csv', 'rU');
countries = open('data/countries.json', 'r')
gdpfile = open('data/GDP.csv', 'rU')

def get_gdp(year):
    gdpfile.seek(0)
    countries.seek(0)
    country_names = json.loads(countries.read()).keys()
    gdp_dict = {}
    for i in range(5):
        gdpfile.readline()
    reader = csv.reader(gdpfile,delimiter=',')
    for row in reader:
        if str(row[0]) in country_names:
            gdp_dict[str(row[0])] = row[year - 1960 + 4]
    return gdp_dict

def get_year_data(year, maxval):
    year = str(year)
    countries.seek(0)
    csvfile.seek(0)
    csvfile.readline()         #skip the CSV header
    codes = json.load(countries)
    reader = csv.reader(csvfile, delimiter=',')
    edgelist = []
    edgeweights = []
    for row in reader:
        if row[2] == year:
            if row[3] not in codes or row[4] not in codes:
                continue
            if float(row[5]) >= maxval:
                edgelist.append((int(codes[row[3]]), int(codes[row[4]])))
                edgeweights.append(float(row[5]))
            if float(row[6]) >= maxval:
                edgelist.append((int(codes[row[4]]), int(codes[row[3]])))
                edgeweights.append(float(row[6]))
    return (edgelist, edgeweights)
