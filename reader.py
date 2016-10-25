import csv
import json
csvfile = open('GDP.csv', 'rU');
countries = open('countries.json', 'r')

def getGDP(year):

    csvfile.readline();
    s = countries.read()
    c = json.loads(s)

    list = c.keys()
    #print 'Canada' in list

    reader = csv.reader(csvfile,delimiter=',')
    i = 0
    count = 0
    list2 = []
    for row in reader:
        if row !=[] and i > 3:
            if str(row[0]) in list:
                list2.append([row[0],row[year - 1960 + 4]])
        i = i + 1

    print list2[0]
    #difference = []
    #for i in range(0 , len(list)):
    #    if list[i] not in list2:
    #        difference.append(list[i])
    #print len(difference)
    #print difference
    return list2

getGDP(2000)