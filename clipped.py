import numpy as np
import scipy.io.wavfile as wave
import sounddevice as sd

# step 1 - write a sine wave to a wav file
# get wave specs

frequency = 440
rate = 48000
duration = 1

#create chunks
time = np.linspace(0, duration, rate*duration)
#create values at those chunks
regular = np.sin(2*np.pi * frequency * time)

#get maximum value of 16 bits
maxshort=np.iinfo(np.short).max
#scale to 1/4 of max value
regular = (maxshort/4) * regular

#cast values to shorts
regular = regular.astype(np.short)

#save to file
wave.write('sine.wav', rate, regular)

#step 2 - create clipped wave and save to wav file
clipped = np.sin(2*np.pi * frequency * time)
#scale to 1/2 of max value
clipped = (maxshort/2) * clipped
#cast to shorts
clipped = clipped.astype(np.short)

#loop through sine, clip values
i = 0
while i < len(clipped):
    if clipped[i] > 8192:
        clipped[i] = 8192
    elif clipped[i] < -8192:
        clipped[i] = -8192
    i += 1

#save to file
wave.write('clipped.wav', rate, clipped)

#step 3 - play the clipped sine through system
sd.play(clipped, samplerate=rate)
sd.wait()