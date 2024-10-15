# this was just a test script for speech recognition, keeping for documentation purposes:)

import speech_recognition as sr

def test_recognize_google():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Please provide your feedback:")
        audio = recognizer.listen(source)
        try:
            feedback = recognizer.recognize_google(audio)
            print(f'Feedback received: {feedback}')
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")

if __name__ == '__main__':
    test_recognize_google()
