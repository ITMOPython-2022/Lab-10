from vosk import Model, KaldiRecognizer
import json
import wave
import pyttsx3

model = Model('vosk-model-small-ru-0.4')

wf = wave.open('demo.wav', "rb")
rec = KaldiRecognizer(model, 32000)

result = ''
last_n = False

while True:
    data = wf.readframes(32000)
    if len(data) == 0:
        break

    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())

        if res['text'] != '':
            result += f" {res['text']}"
            last_n = False
        elif not last_n:
            result += '\n'
            last_n = True

res = json.loads(rec.FinalResult())
result += f" {res['text']}"

print(result)

#Works only on MacOS
engine = pyttsx3.init('nsss')
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.yuri')
engine.say(result)
engine.runAndWait()