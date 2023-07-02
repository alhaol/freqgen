import os
import streamlit as st

# Folder where MP3 files are stored
music_folder = "./"

def list_all_mp3s(music_folder):
    """List all MP3 files in the specified directory"""
    return [f for f in os.listdir(music_folder) if f.endswith('.mp3')]

def main():
    st.title("MP3 Player App")

    st.write("""
    Welcome to this simple MP3 Player App. 
    You can upload an MP3 file from your device, or choose from the existing files below to play in the browser.
    """)

    # File uploader allows user to upload their own MP3 file
    audio_file = st.file_uploader("Upload an MP3 File", type=['mp3'])
    
    if audio_file is not None:
        # Save the uploaded file to the music_folder directory with the same name as uploaded
        with open(os.path.join(music_folder, audio_file.name), 'wb') as f:
            f.write(audio_file.getvalue())
        st.success(f"File upload successful! Saved under {audio_file.name}")

        # Display a audio player widget
        st.audio(audio_file, format='audio/mp3')
        st.write("Enjoy your music! 🎵")

    # List all existing MP3 files in the music folder
    mp3_files = list_all_mp3s(music_folder)
    if mp3_files:
        st.write("Or choose from the existing MP3 files:")
        selected_file = st.selectbox("", mp3_files)
        st.audio(os.path.join(music_folder, selected_file), format='audio/mp3')

if __name__ == "__main__":
    main()

#streamlit run --server.address 0.0.0.0 
