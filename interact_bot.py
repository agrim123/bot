def interact_bot(argv):
	if argv[1] == '-h':
		help()
	elif argv[1] == 'sysinfo':
		print os.getlogin()
		print platform.machine()
		print platform.version()
		print platform.system()
		print platform.processor()
	else:
		print "Not Recognized"