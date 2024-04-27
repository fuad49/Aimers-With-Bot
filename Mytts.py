from gtts import gTTS
from langdetect import detect
from playsound import playsound
import os

fileName = 'Voice'

def PlayNarration(text):
    try:
        langDet = detect(text)
        voice = gTTS(text, lang=langDet)
        namePath = ''.join([fileName, langDet, ".mp3"])
        voice.save(namePath)
        playsound(namePath)
    except Exception as e:
        print("Error:", e)
    finally:
        if os.path.exists(namePath):
            os.remove(namePath)

