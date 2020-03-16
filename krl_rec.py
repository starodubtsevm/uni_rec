#!/usr/bin/env python3
from receiver import*
from limiter import*
from comparator import*
from decode import*
from pll2 import*
from fsk_delay_det import*

#---------------------------------------
class krl(receiver):
    "Класс приемника сигнала КРЛ"

    def __init__(self):
        """Инициализация класса"""
        super(krl,self).__init__()
        self.frequency = 525
        self.code = 0x2C
        self.limiter = limiter(2,2)
        self.det = fsk_det(19.55)
        #self.det_iir = det_iir()
        self.comp_det =comparator(-0.1,0.1, 1)
        self.sem_pll = pll2(1)
        self.decode = decode()

    def procesing(self, data):
        """Обработка сигнала. Вычисление rms"""

        for i in range(len(data)):
            print (data[i])
            #temp1 = chan_fir.proc(sample)        # filtered signal
            temp2 = self.limiter.proc(data[i])         # signal after limiter
            temp3 = self.det.proc(temp2)               # signal after fsk det
            #temp4 = self.det_iir.filter(temp3)         # signal after fsk det filter
            temp5 = self.comp_det.proc(temp4)          # signal after comparator
            sync,err,bit = selfsem_pll.proc(temp5)    # signal after pll
            if sync == 1:
                temp12 = self.decoder1.proc(bit)       # signal after decoder
            else:
                pass
        return

