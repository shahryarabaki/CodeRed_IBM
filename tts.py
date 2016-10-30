import os
def tts(filename):
  USER = '4e0bdd47-de43-4a54-a79a-04575912d7fe';
  PASS = 'tm4pkowU2Qlp';
  return os.popen('curl -X POST -u "' + USER  + ":" + PASS + '" --header "Content-Type: audio/wav" --data-binary @' + filename + ' "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?timestamps=true&word_alternatives_threshold=0.9&continuous=true"').read()
