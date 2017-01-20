def bot_cli(argv):
	while(1):
		arg = raw_input("Bot >>  ")
		if(arg == 'yo'):
			print "YO !!"
		elif(arg =="exit"):
			print "Bye Bye!!"
			exit()
		else:
			print "Unknown"