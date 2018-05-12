import json
import csv
from collections import Counter

p=open("prevent.json", "r")
pdata= p.read()


preventData = json.loads(pdata)
pvt_data = preventData['items']

def pvt():

	prevent= []

	counter=Counter()

	for item in preventData['items']:
		for link in item['Links']:
			if link['Key'] == "SEC-1863":
				newKey = (item['Key'])
				newRating =(item['Rating'])
				print(newRating)
				if newRating == 'High':
					counter['preventHigh']+=1
				


	prevent.append(counter['preventHigh'])


	print(prevent)
pvt()

for p in preventData['items']:
	fo = Open(r['Key']+"_"+r['Rating']+".txt", wb)
	fo.write(r)


	print (p['Key'])





