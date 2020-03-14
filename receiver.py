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

            shift = len(data)
            print (shift)

#            if self.calc(data) == 0:
#                 raise SystemExit

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
        self.channel = "both"
        self.start_idx = 0
        self.fs = fs
        if self.channel == "left" or self.channel == "both":
            self.A_l = 1
        else:
            self.A_l = 0
        if self.channel == "right" or self.channel == "both":
            self.A_r = 1
        else:
            self.A_r = 0

