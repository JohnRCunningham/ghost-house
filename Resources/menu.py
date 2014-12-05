from gameMenuInput import *

def menu(debug = False):
	if debug:
		print "Welcome to Madlibs Debug"
	selection = ""
	while selection != "exit":
		print "***********Madlibs***********"
		print "* Start Game                *"
		print "* options                   *"
		print "* exit                      *"
		print "* ------------------------- *"
		print "* Please type a selection   *"
		selection = getMenuOption(debug)
		print "*****************************"
		
		if selection == "1":
			level1(debug)
menu(False)

