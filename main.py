'''import speech_recognition as ses_tanimla

sesi_tanimla = ses_tanimla.Recognizer()


with ses_tanimla.AudioFile('sesornek.wav') as ses_dosyasi:
    sesi_dinle = sesi_tanimla.listen(ses_dosyasi)

    yazi = sesi_tanimla.recognize_google(sesi_dinle, language="tr-TR")
    print(yazi)
'''


import speech_recognition as sr
                        #You can shorten the name of your library.



r = sr.Recognizer()


with sr.AudioFile('yourpath.wav') as source:
    audio_text = r.listen(source)
    text = r.recognize_google(audio_text, language= "tr-TR")
                                        #you can change language
    print(text)

