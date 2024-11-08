#%% Import the required libraries
import pickle
import time
import simpleaudio as sa
import numpy as np
from scipy.io.wavfile import write

#%% Generate a beep sound and save it as 'metronome_click.wav'
def generate_beep(frequency=440, duration=0.1, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    beep = np.sin(frequency * t * 2 * np.pi)
    beep = (beep * 32767).astype(np.int16)
    write('metronome_click.wav', sample_rate, beep)

generate_beep()

#%% Read the healthy controls pickle file
# Replace 'your_pickle_file.pkl' with the path to your pickle file
pickle_file_path = 'datasets/healthy controls/5f4888a8-4063-4044-bf39-b5b50b8111bb_heart_rate.pickle'

# Open the pickle file in binary read mode
with open(pickle_file_path, 'rb') as file:
    data = pickle.load(file)

# Print the content of the pickle file
print(data)

hr = data['value'].mean()

# Print the hr value as a whole number
print(f"Average Heart rate (hr): {hr:.2f}")

#%% Generate metronome sound based on hr
def generate_metronome(bpm):
    # Calculate the interval in seconds
    interval = 60.0 / bpm
    
    # Load the generated beep sound
    wave_obj = sa.WaveObject.from_wave_file('metronome_click.wav')
    
    # Print the BPM as a whole number
    print(f"Metronome is playing at the BPM: {bpm:.0f}")
    
    while True:
        play_obj = wave_obj.play()
        play_obj.wait_done()
        time.sleep(interval)

# Start the metronome
generate_metronome(hr)
