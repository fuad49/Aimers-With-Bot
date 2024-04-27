from googletrans import Translator

def TranslateIt(sText, lang):
    print(lang)
    translator = Translator()
    out =  translator.translate(sText, dest=lang)

    return out.text