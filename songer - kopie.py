import numpy as np
from scipy.io.wavfile import write
from pprint import pprint
import numpy as np
import simpleaudio as sa

def get_wave(freq, duration=0.5):
    '''
    Function takes the "frequecy" and "time_duration" for a wave 
    as the input and returns a "numpy array" of values at all points 
    in time
    '''
    
    amplitude= 9999999999999999
    t = np.linspace(0, duration, int(samplerate * duration))

    note = 0.8*np.sin(1*freq*t*np.pi)*np.exp(-2*t)
    note += 0.6*np.sin(2*freq*t*np.pi)*np.exp(-2*t)
    note += 0.4*np.sin(3*freq*t*np.pi)*np.exp(-2*t)
    note += 0.2*np.sin(4*freq*t*np.pi)*np.exp(-2*t)


    wave = note

    return wave
"""
    note = 0.6*np.sin(1*7*freq*t)*np.exp(-0.00015*t*np.pi*2)
    note += 0.03*np.sin(2*7*freq*t)*np.exp(-0.00015*t*np.pi*2)
    note += 0.02*np.sin(3*7*freq*t)*np.exp(-0.00015*t*np.pi*2)
    note = note*note*note
    note *= 1 +2*t*np.exp(0.000015*t)
    note *= 1 +16*t*np.exp(-10*t)
    wave = note
"""    
    


def get_piano_notes():
    '''
    Returns a dict object for all the piano 
    note's frequencies
    '''
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 261 #Frequency of Note C4
    
    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}        
    note_freqs[''] = 0.0 # silent note
    
    return note_freqs


def get_song_data(music_notes):
    '''
    Function to concatenate all the waves (notes)
    '''
    note_freqs = get_piano_notes() # Function that we made earlier
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song


samplerate = 44100 #Frequecy in Hz





  
# To get the piano note's frequencies
note_freqs = get_piano_notes()
pprint(note_freqs)
'''
           {'': 0.0,
           'A': 440.00745824565865,
           'B': 493.8916728538229,
           'C': 261.63,
           'D': 293.66974569918125,
           'E': 329.63314428399565,
           'F': 349.2341510465061,
           'G': 392.0020805232462,
           'a': 466.1716632541139,
           'c': 277.18732937722245,
           'd': 311.1322574981619,
           'f': 370.00069432367286,
           'g': 415.31173722644}
 '''



music_notes = 'C-E-G--C-E-G--'
"""
music_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C'
"""
data = get_song_data(music_notes)

# Ensure that highest value is in 16-bit range
audio = data * (2**15 - 1) / np.max(np.abs(data))
# Convert to 16-bit data
audio = audio.astype(np.int16)

# Start playback
play_obj = sa.play_buffer(audio, 1, 2, samplerate)

# Wait for playback to finish before exiting
play_obj.wait_done()


data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)


write('twinkle-twinkle7.wav', samplerate, data.astype(np.int16))
