from help_cli import *

def interact_bot(argv):
	if argv[1] == '-h':
		help_cli()
	else:
		print "Not Recognized"