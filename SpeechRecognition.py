import speech_recognition as sr



def Recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)

        text = recognizer.recognize_google(audio)
        text = text.lower()
        print(f"Recognized {text}")
        return text