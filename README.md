# clipped

Toy program to clip a sine wave.

Initial setup for work on this task required familiarity with a library that manipulated wav files. The reccomended libraries -- scipy.io.wavfile and sounddevice -- were all that needed to be researched. I was already familiar with numpy and only needed a refresher on how linspace worked.

The process can be viewed through comments, but in order to create a wave the steps were: - create a np array of 48000 slices between 0 and 1 (for 1 second) - create a np array of sine values corresponding to each slice - scale the np array to 1/4 the maximum values of a short, instead of -1 to 1 - recast the array contents to shorts - save the file

The process went rather smoothly. I only realized towards the end while writing this that I had not played the sine wave directly, but as a saved file. After fixing that with the sounddevice library, this is complete.
