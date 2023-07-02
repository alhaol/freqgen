
import numpy as np
from scipy.io.wavfile import write
import os
import subprocess

def generate_sound(frequency, duration=1.0, sample_rate=44100, amplitude=0.5, file_name="sound"):
    # Create an array for the time points
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # Generate the sound wave
    note = np.sin(frequency * t * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) * amplitude
    audio = audio.astype(np.int16)

    # Write to a wav file
    write(file_name + '.wav', sample_rate, audio)

    # Convert wav to mp3 using ffmpeg
    command = ['ffmpeg', '-i', file_name + '.wav', file_name + '.mp3']
    subprocess.run(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

    # Remove the wav file
    os.remove(file_name + '.wav')

# Generate a 440 Hz sound
generate_sound(frequency=23000,duration=60*15, file_name="sound_23000_15min")

