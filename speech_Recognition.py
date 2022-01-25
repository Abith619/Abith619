import speech_Recognition as sr
import pyttsx3
listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize.google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
except:
    pass
