import speech_recognition as sr
from google_trans_new import google_translator
import pyttsx3

r = sr.Recognizer()

translator = google_translator()

engine = pyttsx3.init()

source_lang = "fr"
target_lang = "en"


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Parlez quelque chose...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language=source_lang)
        print("Vous avez dit:", text)
        result = translator.translate(text,lang_tgt='en',lang_src='fr')
        print("Traduction:", result)
        engine.say(result)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris.")
    except sr.RequestError as e:
        print("Désolé, il y a eu une erreur de service:")
