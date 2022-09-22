import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
  print(voice)
  engine.setProperty('voice', voice.id)
  engine.say('Esse é um teste de audio.')
  engine.runAndWait()