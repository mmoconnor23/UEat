from user import *

def main():
	name = raw_input("Please enter your name: ")
	location = raw_input("Please enter the name of the dining hall you're in: ")
	user = User(name, location)
	user.printName()
	user.printLocation()
	user.changeLocation("Kohlberg Coffee Bar")
	print "Changing Location..."
	user.printLocation()
if __name__ == "__main__":
    main()
