"""
  must have ffmpeg and also espeak installed in the OS
"""
import PyPDF2, pyttsx3, os, platform

FOLDER_INPUT = './input'
FOLDER_OUTPUT = './output'
entries = [x for x in os.listdir(FOLDER_INPUT) if '.pdf' in x.lower()]

speak = pyttsx3.init()
os_running = platform.system().lower()
if os_running == "darwin":
  print('running on Mac')
  speak.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")
elif os_running == 'linux':
  print('running on Linux')
  # test voices and select best
  # speak.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")
elif os_running == 'windows':
  print('running on Windows')
  # test voices and select best
  # speak.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")

for entry in entries:
  pathPdf = f'{FOLDER_INPUT}/{entry}'
  pathSound = f'{FOLDER_OUTPUT}/{entry.replace(".pdf", ".mp3")}'
  if os.path.exists(pathSound):
    continue
  print(f'transforming {entry} file to mp3')

  pdfFile = open(pathPdf, 'rb')
  pdfReader = PyPDF2.PdfFileReader(pdfFile)
  book = [pdfReader.getPage(page).extractText() for page in range(pdfReader.numPages)]

  try:
    speak.save_to_file('. \n'.join(book), pathSound)
    speak.runAndWait()
  except Exception as e:
    print(e)
speak.stop()