# ==== Text to Speech using pyttsx3 (Offline TTS) ====

# Import the pyttsx3 library
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Define the text you want the bot to speak
text = "Assalamualaikum! My name is Aisha. Welcome to my Text to Speech bot."

# Set the speaking rate (default is ~200 words per minute)
engine.setProperty('rate', 150)

# Set the volume level (0.0 to 1.0)
engine.setProperty('volume', 1.0)

# Get the list of available voices
voices = engine.getProperty('voices')

# Set the voice to female (index 1 is usually female, 0 is male)
engine.setProperty('voice', voices[1].id)

# Queue the text to be spoken
engine.say(text)

# Process the voice queue and speak the text
engine.runAndWait()


# ==== List all available voices ====

# Re-initialize the engine to list voices (optional)
engine = pyttsx3.init()

# Print all available system voices with index numbers
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name}")

# Save the spoken text to an audio file using pyttsx3 (offline)
engine.save_to_file(text, 'aisha_voice.mp3')
engine.runAndWait()


# ==== Text to Speech using Google TTS (gTTS - Online) ====

# Import gTTS and os modules
from gtts import gTTS
import os

# Define the text to be converted to speech
text = "Assalamualaikum! My name is Aisha. Welcome to my bot."

# Create a gTTS object (language is English)
tts = gTTS(text, lang='en')

# Save the audio file in MP3 format
tts.save("aisha_voice.mp3")

# Play the saved MP3 file (for Windows use 'start', Mac: 'afplay', Linux: 'mpg123')
os.system("start aisha_voice.mp3")
