from re import split
from flask import Flask,render_template,request 
from flask_bootstrap import Bootstrap
import test
import videoTester
import voiceAnalyzer
import time
import pyaudio
import os
import wave
from models import Model
import Final_Result
import sentiment_predict_tweet

app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def inde():
    return render_template("index.html")

@app.route('/qstn')
def phq():
    return render_template("phq9.html",data="Anxiety and Depression Detection")

@app.route('/expression') 
def expression():
    p=videoTester.exp()
    if(p=="Anxious"):
        depression=1
    
    if(p=="Depressed"):
        depression=2
    
    if(p=="Normal"):
        depression=0
    
    with open('videocheck.txt', 'w') as f:
        f.write(str(depression))
    
    return render_template("face.html",data=p)


@app.route('/face') 
def face():
    return render_template("face.html",data = "Anxiety and Depression Detection")

@app.route('/voice')
def voice():
    return render_template("voice.html",data = "Click on the Mic to Record",Detect="Detect",ref="voice_analyzer")

@app.route('/quiz')
def quiz():
    return render_template("quiz1.html",data = "Anxiety and Depression Detection")

@app.route('/voice_recording')
def voice_recording():
    CHUNK = 1024 
    FORMAT = pyaudio.paInt16 #paInt8
    CHANNELS = 2 
    RATE = 44100 #sample rate
    RECORD_SECONDS = 4
    WAVE_OUTPUT_FILENAME = "output10.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK) #buffer

    #return render_template("voice.html", data = "Recording ....")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data) # 2 bytes(16 bits) per channel

    

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return render_template("voice.html", data = "Done recording.",Detect="Detect",ref="voice_analyzer")
    
@app.route('/voice_analyzer')
def voice_analyzeer():
    res = voiceAnalyzer.alalyzer()
    res2 = os.system('python test.py -f output10.wav > output.txt')
    file =  open("output.txt","r")
    #gender = ["male","female"]
    for line in file:
        if "Result:" in line:
            sound = line.split()
            res2 = sound[1]
    if(res=="Happy"):
        depression=0
      
    if(res=="Anxious"):
        depression=1
    if(res=="Depressed"):
        depression=2
    if(res!="Happy" and res!="Anxious" and res!="Depressed"):
        depression=0
    with open('voicecheck.txt', 'w') as f:
        f.write(str(depression))
    return render_template("voice.html",data = res, Detect="Next",ref="face")
@app.route('/quiz_new')
def quiz_new():
    return render_template("quiz1.html",data = "Anxiety and Depression Detection")
@app.route('/predict', methods=["POST"])
def predict():
    q1 = int(request.form['a1'])
    q2 = int(request.form['a2'])
    q3 = int(request.form['a3'])
    q4 = int(request.form['a4'])
    q5 = int(request.form['a5'])
    q6 = int(request.form['a6'])
    q7 = int(request.form['a7'])
    q8 = int(request.form['a8'])
    q9 = int(request.form['a9'])
    q10 = int(request.form['a10'])

    values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    model = Model()
    classifier = model.svm_classifier()
    prediction = classifier.predict([values])
    depressed=0
    if prediction[0] == 0:
            result = 'Your Depression test result : No Depression'
            depressed=0
    if prediction[0] == 1:
            result = 'Your Depression test result : Mild Depression'
            depressed=1
    if prediction[0] == 2:
            result = 'Your Depression test result : Moderate Depression'
            depressed=2
    if prediction[0] == 3:
            result = 'Your Depression test result : Moderately severe Depression'
            depressed=3
    if prediction[0] == 4:
            result = 'Your Depression test result : Severe Depression'
            depressed=4
    with open('quizcheck.txt', 'w') as f:
        f.write(str(depressed))
        f.close()
    return render_template("result.html", result=result)

@app.route('/sentiment')
def sentiment():
    return render_template("sentiment.html",data="Anxiety and Depression Detection")
@app.route('/text', methods=["POST"])
def text():
    text = request.form['form10']
    predictt= sentiment_predict_tweet.RunNew(text)
    print(predict)
    if(predictt=="Positive"):
        res="Your input is Positive"
        depressed=0
    if(predictt=="Negative"):
        res="Your input is Negative"
        depressed=1
    if(predictt=="Neutral"):
        res="Your input is Neutral"
        depressed=0
    with open('texttweet.txt', 'w') as f:
        f.write(str(depressed))
    return render_template("result1.html", result=predictt)
    
@app.route('/finalresult')
def finalresult():
    fresult = Final_Result.finalres()
    return render_template("finalresult.html",result=fresult)
    