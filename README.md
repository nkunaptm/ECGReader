# ECGReader
ECGReader code, java and python code utilized in creating a GUI for reading an ECG signal from the Line-In port. 

The ECGRecorder.java file is java code for reading an ECG signal and saving it as a .wav file named ECG.wav, the GUI contains 2 buttons, a capture and a stop button. When the capture button is pressed the ECG signal coming in from the line-in port starts to get recorded. once the user presses the stop button the code stops recording and saves an ECG.wav file. 


The show.py file is python code for displaying an audio file which contains an ECG signal.

The recorder.py is python code for recording and saving an ECG signal from the line-in port of a PC as a audio file.

The ECGReader.py file is python code for a GUI, depending on the input the GUI either captures an ECG signal and saves it or displays an already saved ECG signal. The first blank space takes in the name of the ECG signal you want to create, the record button when pressed records an ECG signal and saves it and the name in the first space, a notification is then given once recording is done. the second input space is for the name of an already recorded ECG signal that the user wants to display, when the view button is pressed a new window with the ECG signal pops up.
