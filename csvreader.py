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
    csvfile.readline()
    codes = json.load(countries)
    reader = csv.reader(csvfile, delimiter=',')
    edgelist = []
    for row in reader:
        if row[2] == year:
            if row[3] not in codes or row[4] not in codes or float(row[5]) < maxval or float(row[6]) < maxval:
                continue
            edgelist.append((int(codes[row[3]]), int(codes[row[4]])))
    return edgelist
