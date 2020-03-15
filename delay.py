import numpy as np
from const import *

f     = 475
fdev  = fmod
Tstop = 50e-3
N     = int(Tstop/(1/fs))

def calc(f):

    Diff     = 0
    Del_max  = 0
    Diff_max = 0

    for i in range (N):
        delay = 1.0/fs * i
        Diff = np.cos(2*np.pi*(f-fdev)*delay) - np.cos(2*np.pi*(f+fdev)*delay)
        #print (delay, Diff)

        if Diff > Diff_max:
            Diff_max = Diff
            Del_max = delay

    return Diff_max, Del_max, int(Del_max/(1/fs))

print (calc(f))

