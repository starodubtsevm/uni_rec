#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class IIR2Filter(object):

    def __init__(self,order,cutoff,filterType,design='butter',rp=1,rs=1,fs=0):
        ''' инициализация iir фильтра'''
        self.COEFFS = self.createCoeffs(order,cutoff,filterType,design,rp,rs,fs)
        self.acc_input = np.zeros(len(self.COEFFS))
        self.acc_output = np.zeros(len(self.COEFFS))
        self.buffer1 = np.zeros(len(self.COEFFS))
        self.buffer2 = np.zeros(len(self.COEFFS))
        self.input = 0
        self.output = 0

    def filter(self,input):
        '''фильтрация сигнала'''
        #len(COEFFS[0,:] == 1 means that there was an error in the generation 
        #of the coefficients and the filtering should not be used
        
            self.input = input
            self.output = 0

            #The for loop creates a chain of second order filters according to 
            #the order desired. If a 10th order filter is to be created the 
            #loop will iterate 5 times to create a chain of 5 second order 
            #filters.
            for i in range(len(self.COEFFS)):

                self.FIRCOEFFS = self.COEFFS[i][0:3]
                self.IIRCOEFFS = self.COEFFS[i][3:6]

                #Calculating the accumulated input consisting of the input and 
                #the values coming from the feedbaack loops (delay buffers 
                #weighed by the IIR coefficients).
                self.acc_input[i] = (self.input + self.buffer1[i] 
                * -self.IIRCOEFFS[1] + self.buffer2[i] * -self.IIRCOEFFS[2])

                #Calculating the accumulated output provided by the accumulated
                #input and the values from the delay bufferes weighed by the 
                #FIR coefficients.
                self.acc_output[i] = (self.acc_input[i] * self.FIRCOEFFS[0]
                + self.buffer1[i] * self.FIRCOEFFS[1] + self.buffer2[i] 
                * self.FIRCOEFFS[2])

                #Shifting the values on the delay line: acc_input->buffer1->
                #buffer2
                self.buffer2[i] = self.buffer1[i]
                self.buffer1[i] = self.acc_input[i]

                self.input = self.acc_output[i]

            self.output = self.acc_output[i]

        return self.output

