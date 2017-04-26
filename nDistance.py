#Author : Joonho Park, Chris Kim, Tyler Park, Taejin Kim

from lib import * 
import node

def getScore(ns,xCor, yCor):
	count = 0
	for n in ns.values():
		d = n.dHat
		px = n.xCor
		py = n.yCor
		if (getDistance(xCor,px,yCor,py)<d):
			count+=1
	
	return count*1.0/len(ns.values())


