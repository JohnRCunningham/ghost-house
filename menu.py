from menuInput import *
#from sk import *

def menu(debug = False):
	if debug:
		print "Ghost House"
	selection = ""
	while selection != "exit":
		print "*********Ghost House*********"
		print "* 1) Start Game             *"
		print "* 2) Level Select           *"
		print "* 3) Pax Select             *"
		print "* 4) Options                *"
		print "* 5) Exit                   *"
		print "* ------------------------- *"
		print "* Please type a selection   *"
		selection = getMenuOption(debug)
		print "*****************************"
		
		if selection == "1":
			pygame.init()
		if selection == "2":
			print "In progress..."
		if selection == "3":
			print "In progress..."	
		if selection == "4":
			print "Not available... yet..."
		if selection == "5":
			print "Press a key to exit."	
			exit()
menu(False)
