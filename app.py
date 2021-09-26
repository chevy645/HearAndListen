from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import os
from google.cloud import speech


app = Flask(__name__)

#This method will return what should be returned on the homepage

@app.route("/", methods=["GET", "POST"])
def index():
   os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "pelagic-rig-327114-388e59ecc397.json"
   speech_client = speech.SpeechClient()
   transcript = ""
   if request.method == "POST":
       print("FORM DATA RECEIVED")

       #file does not exist or the file is blank
       if "file" not in request.files:
           return redirect(request.url)

       #if a file exists it will give me the file
       file = request.files["file"]
       if file.filename == "":
           return redirect(request.url)

       if file:
           recognizer = sr.Recognizer()
           audioFile = sr.AudioFile(file)
           with audioFile as source:
               data = recognizer.record(source)
           transcript = recognizer.recognize_google(data, key=None)
           print(transcript)

   return render_template('index.html', transcript = transcript)

if __name__ == "__main__":
   app.run(debug = True, threaded=True)



