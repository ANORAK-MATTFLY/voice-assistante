import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('say something')
    audio = r.listen(source)
    try:
        voice_data = r.recognize_google(audio)
        print(voice_data)
    except sr.UnknownValueError:
        print('Sorry I did not get that')
    except sr.RequestError:
        print('sorry, my speech service is down')
        
        