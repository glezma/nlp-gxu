import speech_recognition as sr

# %%  Reading from audio file
filename = "16-122828-0002.wav"

# initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
# %% Reading from microphone

## Windows
# pip3 install pyaudio

## Linux
# sudo apt-get install python-pyaudio python3-pyaudio
# pip3 install pyaudio

# # Mac OS
# brew install portaudio
# pip3 install pyaudio

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data, language="es-ES")
    print(text)