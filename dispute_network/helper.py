#__author__ = 'dhaval'
import csv
import json

d_file = open('data/MIDA_4.01.csv','r')
d_file.readline()

def getDisputes(year):
    reader = csv.reader(d_file,delimiter=',')
    disputes = []
    for row in reader:
        if int(row[22]) == 1 or int(row[7]) > year:
        #print row
            disputes.append(str(row[0]))
    return disputes
