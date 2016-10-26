#__author__ = 'dhaval'

import requests
import json
payload = {'max':'50000' , 'type' : 'C', 'freq' : 'A' , 'px' : 'HS' , 'ps' :'2013' ,'r' : '826','p':'0','rg':'all','cc':'AG2','fmt'  : 'json'}
r = requests.get('http://comtrade.un.org/api/get' ,params =  payload)
#r = requests.get('https://github.com/timeline.json')
ob =  json.loads(r.text)
#print json.dumps(ob['dataset'],indent=4)
#print json.dumps(ob , indent=4)
print ob['dataset'][0]