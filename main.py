# using numpy generate a sine wave with 1 khz frequency and 1 second duration

import numpy as np

# Write a simple function to generate a sine wave with a given frequency and duration

def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    return wave

wave = generate_sine_wave(1000, 2, 100)
print(type(wave))
print(wave.shape)
print (wave)
print("abdulla making changes in parallel to the smae file")