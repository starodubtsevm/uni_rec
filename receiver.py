#!/usr/bin/env python3
from const import*

#---------------------------------------
class receiver(object):
    "Класс приемника сигнала"

    def __audio_callback (self,indata, outdata, frames, time, status):
        """callback function"""
        if status:
            print(status, file=sys.stderr)

        t = (self.start_idx + np.arange(frames)) / (sd.default.samplerate)
        t = t.reshape(-1, 1)
        self.start_idx += frames

        self.q.put(indata[::self.downsample, self.mapping])

        while True:
            try:
                data = self.q.get_nowait()
            except queue.Empty:
                break

        data_left  =  data[:,0]
        data_right =  data[:,1]

        if self.A_l == 1:
            data = data_left
        elif self.A_r == 1:
            data = data_right
        else:
            print ("Error. Please select channel", file=sys.stderr)
        self._check_channel()
        self.procesing(data)

    def __init__(self):
        """Инициализация класса"""
        sd.default.blocksize = 0
        sd.default.samplerate = fs
        sd.default.channels = 2
        self.stream = sd.Stream(device = (sd.default.device, sd.default.device),\
                                                 callback = self.__audio_callback)
        self.q = queue.Queue()
        self.downsample = 2
        self.channels = [1,2]
        self.mapping = [c - 1 for c in self.channels]
        self.channel = "left"
        self.A_l = 1
        self.A_r = 0
        self.start_idx = 0
        self.fs = fs
        
    def _check_channel(self):
        '''Проверка установленного канала '''
        if self.channel == "left":
            self.A_l = 1
            self.A_r = 0
        else:
            self.A_l = 0
            self.A_r = 1

        if self.channel == "right":
            self.A_r = 1
            self.A_l = 0
        else:
            self.A_r = 0
            self.A_l = 1

    def procesing(self, data):
        """Обработка сигнала. Вычисление rms"""

        rms = np.sqrt(np.mean(np.square(data)))
        data_mean = np.mean(rms)
        print (data_mean, len(data),self.A_l,self.A_r)

        return

