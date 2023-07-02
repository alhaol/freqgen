import numpy as np
from scipy.io.wavfile import write
import streamlit as st

try:
    import numpy
except ImportError:
    import os
    os.system('pip install numpy')

try:
    import scipy
except ImportError:
    import os
    os.system('pip install scipy')

# Function to generate sine wave
def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=8000):
    x = np.linspace(0, duration, int(sample_rate * duration), False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = amplitude * np.sin(2 * np.pi * frequencies)
    return y.astype(np.int16)  # Convert to 16-bit data

def app():
    st.title('Ibrahim Wave Generator')

    freq = st.slider('Frequency (Hz)', min_value=20.0, max_value=65000.0, value=440.0)
    duration = st.slider('Duration (s)', min_value=0.1, max_value=600.0, value=1.0)

    if st.button('Generate'):
        wave = generate_sine_wave(freq, duration)
        write('sine_wave.wav', 44100, wave)  # Writing the sound to a file
        st.audio('sine_wave.wav', format='audio/wav')

if __name__ == "__main__":
    app()
#streamlit run --server.address 0.0.0.0 genandplay.py
