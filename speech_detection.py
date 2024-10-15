# copilot generated code (needs LOTS of review, but is a starting place for us)
# idea: use most up-to-date speech recognition technology to read audio input from patients
# increases accessibility specifically for elderly and disabled patients

import speech_recognition as sr

def record_voice_feedback():
    recognizer = sr.Recognizer()  # initialize the recognizer
    with sr.Microphone() as source:  # use the mic as audio source
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=180, phrase_time_limit=180)  # set 3 min time limit
        try:
            feedback = recognizer.recognize_google(audio)
            print(f'Feedback received: {feedback}')
            return feedback
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None

def main():
    feedback = record_voice_feedback()
    if feedback:
        print(f'Feedback: {feedback}')

if __name__ == '__main__':
    main()