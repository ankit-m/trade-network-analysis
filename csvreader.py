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

def get_year_data(year, maxval):
    year = str(year)
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
