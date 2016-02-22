from lib import *
import node

def getScore(nodes,xCor, yCor):
	total = 0.0
	for n in nodes.values():
		px = n.xCor
		py = n.yCor

		total += getDistance(xCor,px,yCor,py)/n.frequency
	return total/len(nodes.values())
