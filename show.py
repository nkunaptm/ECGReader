import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('testF.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')


#If Stereo
if spf.getnchannels() == 2:
    print ("Just single channel files")
    sys.exit(0)

#plot the signal on a graph
plt.figure(1)
plt.title('ECGSignal Wave.')
plt.plot(signal)
plt.show()