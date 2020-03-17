import numpy as np
import scipy.signal as signal


def createCoeffs(order,cutoff,filterType,design='butter',rp=1,rs=1,fs=0):

    #defining the acceptable inputs for the design and filterType params
    designs = ['butter','cheby1','cheby2']
    filterTypes1 = ['lowpass','highpass','Lowpass','Highpass','low','high']
    filterTypes2 = ['bandstop','bandpass','Bandstop','Bandpass']

    #Error handling: other errors can arise too, but those are dealt with 
    #in the signal package.
    isThereAnError = 1 #if there was no error then it will be set to 0
    COEFFS = [0] #with no error this will hold the coefficients
 
    if design not in designs:
        print('Gave wrong filter design! Remember: butter, cheby1, cheby2.')
    elif filterType not in filterTypes1 and filterType not in filterTypes2:
        print('Gave wrong filter type! Remember: lowpass, highpass', 
              ', bandpass, bandstop.')
    elif fs < 0:
        print('The sampling frequency has to be positive!')
    else:
         isThereAnError = 0

    #if fs was given then the given cutoffs need to be normalised to Nyquist
    if fs and isThereAnError == 0:
        for i in range(len(cutoff)):
            cutoff[i] = cutoff[i]/fs*2

    if design == 'butter' and isThereAnError == 0:
        COEFFS = signal.butter(order,cutoff,filterType,output='sos')
    elif design == 'cheby1' and isThereAnError == 0:
        COEFFS = signal.cheby1(order,rp,cutoff,filterType,output='sos')
    elif design == 'cheby2' and isThereAnError == 0:
        COEFFS = signal.cheby2(order,rs,cutoff,filterType,output='sos')
    return COEFFS

