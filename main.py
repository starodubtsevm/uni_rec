#!/usr/bin/env python3

from const import*
from receiver import*
from krl_rec import*

#---------------------------------------------------------------------------
rec1 = receiver()
rec2 = krl()
rec1.channel = "right"
rec2.channel = "right"
#---------------------------------------------------------------------------
#rec1.stream.start()
rec2.stream.start()
#---------------------------------------------------------------------------

input("...Press Enter to exit...")
#---------------------------------------------------------------------------

