import sys
import os
import time

#custom scripts

from help import *
from bot_cli import *
from interact_bot import *

def main(argv):
	print time.ctime()
	print "Yo " + os.getlogin() + ' !!!'
	if len(argv) > 1:
		interact_bot(argv)
	else:
		bot_cli()
	

if __name__ == "__main__":
	main(sys.argv)
