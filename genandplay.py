import numpy as np
from scipy.io.wavfile import write
import streamlit as st

# Function to generate sine wave
def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=8000):
    x = np.linspace(0, duration, int(sample_rate * duration), False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = amplitude * np.sin(2 * np.pi * frequencies)
    return y.astype(np.int16)  # Convert to 16-bit data

def app():
    st.title('Wave Generator')

    freq = st.number_input('Frequency (Hz)', min_value=0, max_value=300000, value=100,step=1)

    duration = st.number_input('Duration (s)', min_value=1, max_value=600, value=10,step=1)

    if st.button('Generate'):
        wave = generate_sine_wave(freq, duration)
        write('sine_wave.wav', 44100, wave)  # Writing the sound to a file
        st.audio('sine_wave.wav', format='audio/wav')

if __name__ == "__main__":
    app()
