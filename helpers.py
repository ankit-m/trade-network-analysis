import json

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
