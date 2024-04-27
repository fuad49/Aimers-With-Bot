from googletrans import Translator
from langdetect import detect

def TranslateIt(sText, lang):
    print(lang)
    translator = Translator()
    out =  translator.translate(sText, dest=lang)

    return out.text

def langDetect(text):
    return detect(text)
