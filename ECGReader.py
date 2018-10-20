from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import pyaudio
import tkinter.messagebox

root = Tk()
root.geometry("230x95+500+300")
root.title("ECGReader")
first = StringVar()
second = StringVar()

#Creating a show method for displaying an ECG signal
def show(event):
    #Acquire input for the name of the signal .wav file to be displayed
    gsecond = second.get()
    
    spf = wave.open(gsecond,'r')
    
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

# creating record method for recording an ECG signal    
def record(event):
    
    # set line in parameters
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 10
    #Acquire input for the name of the signal .wav file to be created
    WAVE_OUTPUT_FILENAME = first.get()
    
    #create a pyaudio object that whill be used to read audio data
    p = pyaudio.PyAudio()
    
    #open the pyaduio stream for reading
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    
    print("* recording")
    
    frames = []
    
    # copy the incomind data and save in the frame array
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("* done recording")
    tkinter.messagebox.showinfo("Notification", "Done Recording")
    #close the stream as we are done recording
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    #save audio into a .wav file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()    


#creating the labels, text input and button variables.
label_1 = Label(root, text="Enter new file name")
label_2 = Label(root, text="Enter file to view")
entry_1 = Entry(root, textvariable=first)
entry_2 = Entry(root, textvariable=second)
button1 = Button(root, text="Record")
button2 = Button(root, text="View")

#Placing the labels
label_1.grid(row=0, column=0)
label_2.grid(row=2, column=0)

#Placing the text input
entry_1.grid(row=1,column=0)
entry_2.grid(row=3,column=0)

#Placing the buttons
button1.grid(row=0,column=1)
button2.grid(row=2,column=1)

#Connect buttons to commands
button2.bind("<Button-1>",show)
button1.bind("<Button-1>",record)

root.mainloop()
