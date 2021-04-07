import math as m
import numpy as np
import simpleaudio as sa
from scipy.io.wavfile import write




frequency = int(input("Input  "))  # Our played note will be x Hz
fs = 44100  # 44100 samples per second
seconds = 1  # Note duration of y seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)

# Generate a 440 Hz sine wave
note = 0.8*np.sin(1*frequency*t)*np.exp(-0.0015*frequency*t)
note += 0.6*np.sin(2*frequency*t)*np.exp(-0.0015*frequency*t)
note += 0.4*np.sin(4*frequency*t)*np.exp(-0.0015*frequency*t)
note += 0.2*np.sin(8*frequency*t)*np.exp(-0.0015*frequency*t)
note += 0.1*np.sin(16*frequency*t)*np.exp(-0.0015*frequency*t)
note += note*note*note

# note = np.sin(frequency * t * 2 * np.pi)

# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
# Convert to 16-bit data
audio = audio.astype(np.int16)

# Start playback
play_obj = sa.play_buffer(audio, 1, 2, fs)

# Wait for playback to finish before exiting
play_obj.wait_done()

name = input("Name your file: ")
write(name + '.wav', fs, audio.astype(np.int16))

