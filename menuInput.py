def getMenuOption(debug = False):
	if debug:
		print "getMenuOption Function"
	validInput = False
	while not validInput:
		option = raw_input("> ")
		option = option.lower()
		if option == "1":
			validInput = True
		elif option == "2":
			validInput = True
		elif option == "3":
			validInput = True
		elif option == "4":
			validInput = True
		elif option == "5":
			validInput = True
		else:
			print "please type a valid option"
			validInput = False
	if debug:
		print "Option is:", option
	return option
