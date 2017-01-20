from brain import * 

def bot_cli():
	while(1):
		command = raw_input("Bot >>  ")
		valid_response = brain(command)
		if valid_response:
			print valid_response
		else:
			print "Bye Bye!!"
			exit()