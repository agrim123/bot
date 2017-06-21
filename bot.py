import sys
import os
import time

#custom scripts

from bot_cli import *
from interact_bot import *

def main(argv):
	print time.ctime()
	print """
	      .andBOTAbnn.
           .aABBBAAUUAABBBAn.
          dBP^~"        "~^TBb.
    .   .ABF                YBA.   .
    |  .ABBb.              .dBBA.  |
    |  BBAUAABAbn      adABAAUABA  |
    I  BF~"_____        ____ ]BBB  I
   BOT BAPK""~^YUBb  dABBBBBBBBBB BOT
   BOT BBBD> .andBB  BBUUP^~YBBBB BOT
   BOT ]BBP     "~Y  P~"     TBB[ BOT
    "  `BK                   ]BB'  "
        TBAn.  .d.aAAn.b.  .dBBP
        ]BBBBAAUP" ~~ "YUAABBBB[
        `BBP^~"  .annn.  "~^YBB'
         YBb    ~" "" "~    dBF
          "YAb..abdBBbndbndAP"
           TBBAAb.  .adABBF
            "UBBBBBBBBBBU"
              ]BBUUBBBBBB[
            .adBBb "BBBBBbn.
     ..andAABBBBBBb.ABBBBBBBAAbnn..
.ndAABBBBBBUUBBBBBBBBBBUP^~"~^YUBBBAAbn.
  "~^YUBBP"   "~^YUBBUP"        "^YUP^"
       ""         "~~"
    """
	print "Yo " + os.getlogin() + ' !!!'
	if len(argv) > 1:
		interact_bot(argv)
	else:
		bot_cli()
	

if __name__ == "__main__":
	main(sys.argv)
