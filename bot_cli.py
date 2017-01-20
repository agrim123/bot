from brain import * 

def bot_cli():
	while(1):
		command = raw_input("Bot >>  ")
		if command == 'yo':
			print "YO !!"
		elif any(command in s for s in greetings):
			print "Whats up?"
		elif command =="exit":
			print "Bye Bye!!"
			exit()
		else:
			print "Unknown"