class User(object):
	def __init__(self, name, location):
		self.name = name
		self.location = location
	def changeLocation(self, newLocation):
		self.location = newLocation
	def leaveLocation(self):
		self.location = "not eating"
	def printName(self):
		print "Name:", self.name
	def printLocation(self):
		print "Dining Hall:", self.location
