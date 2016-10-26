#__author__ = 'dhaval'
import csv
import json

d_file = open('data/MIDA_4.01.csv','r')
d_file.readline()

reader = csv.reader(d_file,delimiter=',')
disputes = []
for row in reader:
    if int(row[22]) == 1:
        #print row
        disputes.append(row[0])

print disputes