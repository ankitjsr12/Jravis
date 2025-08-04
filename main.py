import os
import speech_recognition as sr

def speak(text):
    print(f"Speaking: {text}")
    os.system(f'say -v Samantha "{text}"')

def process_command(c):
    c = c.lower()
    if "open google" in c:
        speak("Opening Google")
        os.system("open https://www.google.com")
    elif "open youtube" in c:
        speak("Opening YouTube")
        os.system("open https://www.youtube.com")
    elif "open facebook" in c:
        speak("Opening Facebook")
        os.system("open https://www.facebook.com")
    elif "safari" in c:
        speak("Opening Safari")
        os.system("open -a Safari")
    elif "chrome" in c:
        speak("Opening Chrome")
        os.system("open -a Google\\ Chrome")
    elif "firefox" in c:
        speak("Opening Firefox")
        os.system("open -a Firefox")
    elif "quit" in c:
        speak("Quitting Jravis")
        exit()
    else:
        speak("Sorry, I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Jravis")

    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)

                if word.lower() == "jravis":
                    speak("Jravis is listening")

                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
                        command = recognizer.recognize_google(audio)

                        process_command(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results: {e}")
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")