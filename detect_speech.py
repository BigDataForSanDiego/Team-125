import speech_recognition as sr

def detect_speech():
    recognizer = sr.Recognizer()  # initialize the recognizer
    with sr.Microphone() as source:  # use mic as source
        recognizer.adjust_for_ambient_noise(source)
        print("Please provide your feedback:")
        audio = recognizer.listen(source, phrase_time_limit=180)  # set max duration to 3 minutes
        try:
            feedback = recognizer.recognize_google(audio)
            print(f'Feedback received: {feedback}')
        except sr.UnknownValueError:
            # speech was unintelligible
            print("Sorry, I could not understand the audio. Please try again.")
        except sr.RequestError:
            # API was unreachable
            print("Could not request results; check your network connection.")

if __name__ == '__main__':
    detect_speech()
