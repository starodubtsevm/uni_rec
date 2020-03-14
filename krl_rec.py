#!/usr/bin/env python3
from receiver import*

#---------------------------------------
class krl(receiver):
    "Класс приемника сигнала КРЛ"

    def __init__(self):
        """Инициализация класса"""
        super(krl,self).__init__()
        self.frequency = 475
        self.code = 0x2C

    def procesing(self, data):
        """Обработка сигнала. Вычисление rms"""

        rms  = np.sqrt(np.mean(np.square(data)))
        data_mean = np.mean(rms)
        print (data_mean, len(data))

        return

