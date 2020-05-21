import speech_recognition as sr
import os
from time import ctime
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import webbrowser
import random



reco = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = reco.listen(source)
        voice_data = ''
        try:
            voice_data = reco.recognize_google(audio, language="fr")
        except sr.UnknownValueError:
            speak("Désolé j'ai du mal a comprendre votre requête, pourriez-vous reformuler s’il vous plait ?")
        except sr.RequestError:
            speak("Désolé, mon service de reconnaissance vocal en hors d'atteinte")
        return voice_data


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='fr')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if "quel est ton nom" in voice_data:
        speak("Je préfère rester anonyme tu ne mérites pas de connaitre mon nom, merci")
    if "quelle heure est-il" in voice_data:
        speak(ctime())
    if "recherche" in voice_data:
        search = record_audio("Que voulais vous que je cherche ?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("Voici ce que j’ai pu trouver sur  " + search)
    if "trouve un endroit" in voice_data:
        location = record_audio("Quel endroit voulez-vous que je cherche ?")
        url = "https://www.google.com/maps/place/" + location + '/&amp;'
        webbrowser.get().open(url)
        speak("Voici l'emplcement de " + location)
    if "arrête" in voice_data:
        exit()
        
    
        
time.sleep(1)
speak("Bienvenu cherz apprenants de la Kinshasa digitale a la tout dernière partie de cette veille présenter par semia lusevakio et Ben matanda ici vous apprendrait a créé des logiciels intelligent-tout comme moi amusez-vous bien")
while 1:
    voice_data = record_audio()
    respond(voice_data) 
    print(voice_data) 