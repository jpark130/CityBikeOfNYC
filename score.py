import webber
import nDistance

def getScore(stations,candidate):
	w = webber.getScore(stations,candidate.xCor,candidate.yCor)*200
	n = nDistance.getScore(stations,candidate.xCor,candidate.yCor)
	sup = candidate.support*3
	return n/w+sup
