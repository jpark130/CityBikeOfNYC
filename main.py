import csv
from node import *
from lib import * 
from candidate import * 
from score import *

class Main(object):
	
	def __init__(self, dataPath):
		url = "http://shareaboutsapi-nycdot.herokuapp.com/api/v2/nycdot/datasets/nycbikeshare/places"
		print "Please wait... getting suggestions from users"
		self.candidates = getCandidates(url)
		self.dataPath = dataPath
		self.nodes = {}
		self.stations = set()
		f = open(dataPath, 'rt')
		reader = csv.reader(f)
		print "suggestions loaded!"
		print "Please wait... parsing data..."
		for row in reader:
			if (row[1] == 'tripduration'):
				continue

			d = getDistance(row[7],row[11],row[6],row[10])
			stationIndex = [4,8]
			for i in stationIndex:
				stationID = row[i]

				if (not stationID in self.stations):
					self.nodes[stationID] = Node(row[i+3],row[i+2],d,1,0)
				else: 
					self.nodes[stationID].addFreq(d)

				self.stations.add(stationID)
		print "Parsing data done!"

	@staticmethod
	def run(dataPath):
		instance = Main(dataPath)
		mCandidate = instance.getmax()
		print "top1 \n latitude: %f, longitude: %f" %(mCandidate[1].yCor,mCandidate[1].xCor)
		print "top2 \n latitude: %f, longitude: %f" %(mCandidate[0].yCor,mCandidate[0].xCor)

	def getmax(self):
		maxS = -float("inf")
		maxC = None
		maxS2 = -float("inf")
		maxC2 = None
		for candidate in self.candidates:
			s = getScore(self.nodes,candidate)
			if (maxS < s):
				maxC = candidate
				maxS = s
				if (maxS2 < s):
					maxC = maxC2
					maxS = maxS2
					maxS2 = s
					maxC2 = candidate
		return maxC,maxC2
	
Main.run('data.csv')
