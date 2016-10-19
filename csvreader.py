# rows
# 2 : year
# 3 : country 1
# 4 : country 2
# 5 : 1 -> 2
# 6 : 2 -> 1
import csv
import json

csvfile = open('dyadic.csv', 'rU');
countries = open('countries.json', 'r')

# Uncomment this code to make the countries.json file
# def save_countries():
#     countries = {};
#     count = 0
#     reader = csv.reader(csvfile, delimiter=',')
#     csvfile.readline()
#     for row in reader:
#         if row[3] not in countries and row[3] != "":
#             countries[row[3]] = count
#             count += 1
#     with open('countries.json', 'w') as fp:
#         json.dump(countries, fp, sort_keys=True, indent=4)
# save_countries()

# returns edge list
def get_year_data(year):
    year = str(year)
    csvfile.seek(0)
    csvfile.readline()
    codes = json.load(countries)
    reader = csv.reader(csvfile, delimiter=',')
    edgelist = []
    for row in reader:
        if row[2] == year:
            # print row[3], row[4]
            if row[3] not in codes or row[4] not in codes or float(row[5]) < 500.0 or float(row[6]) < 500.0:
                continue
            edgelist.append((int(codes[row[3]]), int(codes[row[4]])))
    return edgelist

def get_countries():
    codes = json.load(countries)
    countries_array = []
    for i in codes:
        print codes[i]
