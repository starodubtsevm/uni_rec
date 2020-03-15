from const import *

#---------------------------------------
class limiter(object):

    def __init__(self, out_min, out_max):
        """initialization"""
        self.out_min = out_min
        self.out_max = out_max

    def proc(self, sample):
        """limiting"""
        if sample < self.out_min:
            return self.out_min
        elif self.out_min <= sample <= self.out_max:
            return sample
        else:
            return self.out_max
