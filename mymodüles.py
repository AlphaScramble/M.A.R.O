import speech_recognition as sr


def speak(): #dışarıdan alınan sesi algılar ve sesi yazıya dökerek sana döndürür.Bir değişkene atayarak kullanabilirsin
    r=sr.Recognizer()
    with sr.Microphone() as source:
        listen=r.listen(source)
        mean=r.recognize_google(listen,language="tr-TR")
    return mean











































    