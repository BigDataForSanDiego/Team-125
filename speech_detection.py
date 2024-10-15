# copilot generated code (needs LOTS of review, but is a starting place for us)
# idea: use most up-to-date speech recognition technology to read audio input from patients
# increases accessibility specifically for elderly and disabled patients

import speech_recognition as sr
import threading

stop_recording = False

def record_voice_feedback():
    global stop_recording
    recognizer = sr.Recognizer()  # initialize the recognizer

    with sr.Microphone() as source:  # use the mic as audio source
        recognizer.adjust_for_ambient_noise(source)
        print("Please provide your feedback: press 'Enter' to stop recording:")

        def listen():
            global stop_recording
            audio = recognizer.listen(source, timeout=180, phrase_time_limit=180)
            if not stop_recording:
                try:
                    feedback = recognizer.recognize_google(audio)
                    print(f'Feedback received: {feedback}')
                    return feedback
                except sr.UnknownValueError as e:
                    # speech was unintelligible
                    print("Audio could not be understood.")
                    return e
                except sr.RequestError as e:
                    # API was unreachable/unresponsive
                    print("Could not request results; please check network connection")
                    return e



        # start listening in a separate thread
        # listen_thread = threading.Thread(target=listen)
        # listen_thread.start()
        #
        # # wait for user input to stop recording
        # input()
        # stop_recording = True
        # listen_thread.join()

def main():
    record_voice_feedback()

if __name__ == '__main__':
    main()