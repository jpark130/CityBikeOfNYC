
#Author : Joonho Park, Chris Kim, Tyler Park, Taejin Kim

class Node():

	def __init__(self,xCor,yCor, dHat, frequency,support):
		self.support = support
		self.xCor = xCor
		self.yCor = yCor
		self.dHat = dHat
		self.frequency = frequency

	def addFreq(self,d):
		self.frequency = self.frequency + 1
		self.calculateDHat(d)
	
	def calculateDHat(self,d):
		total = self.dHat * (self.frequency-1) + d
		assert type(total) == float
		return total/(self.frequency)
