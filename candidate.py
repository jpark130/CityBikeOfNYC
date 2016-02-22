import urllib, json
from node import * 

url = "http://shareaboutsapi-nycdot.herokuapp.com/api/v2/nycdot/datasets/nycbikeshare/places"

def getCandidates(url):
	nodes = set()
	response = urllib.urlopen(url)
	data = json.loads(response.read())

	if (data['metadata'][u'next'] != None):
		s = len(data['features'])
		for i in range(s):
			try:	
				support = data['features'][i]['properties'][u'submission_sets'][u'support'][u'length']
				if (support > 20):
					x= data['features'][i][u'geometry'][u'coordinates'][0]
					y= data['features'][i][u'geometry'][u'coordinates'][1]
					nodes.add(Node(x,y,0,1,support/159.0))
			except :
				pass
		nodes = nodes.union(getCandidates(data['metadata'][u'next']))
			
			
	return nodes

