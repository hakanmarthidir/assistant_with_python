import os
import pyttsx3
import speech_recognition as sr


class AssistantCore:
    engine = None
    voices = None

    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        self.sayHello()
        self.startListen()

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def sayHello(self):
        self.speak("Welcome Boss! How can i help you?")

    def catchCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("I'm Listening...")
            audio = r.listen(source)
            try:
                print("Scanning...")
                query = r.recognize_google(audio, language='en')
                print('You said that : ' + query)
            except:
                print("I could not understand, say again please...")
                return ''
            return query.lower()

    def findCommand(self, query):
        if 'music time' in query:
            os.startfile('spotify.exe')
        elif 'open visual studio' in query:
            self.speak('i am opening your file')
        elif 'send email' in query:
            return
        #   .... add more ...

    def startListen(self):
        while True:
            query = self.catchCommand()
            print(query)
            self.findCommand(query)


