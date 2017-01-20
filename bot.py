import sys
import platform
import os
import time

#custom scripts

from help import *
from bot_cli import *

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
def main(argv):
	print time.ctime()
	if len(argv) > 1:
		interact_bot(argv)
	else:
		bot_cli(argv)
	

if __name__ == "__main__":
	main(sys.argv)
