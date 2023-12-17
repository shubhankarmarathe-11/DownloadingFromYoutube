from download import app
from pytube import YouTube
from flask import redirect,render_template,flash,request,send_file
import time


@app.route('/')
def index():
    # flash("Welcome To YouTube Converter")
    return render_template('index.html')


@app.route('/convert/mp4',methods=['GET','POST'])
def convertmp4():
    if request.method == "POST":
        link = request.form['link']
        flash("Converting Video Please Wait .....")
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        yd.download(filename = "./upload/video/outputfile.mp4")
        flash("Video Converted Successfully")
        return send_file(path_or_file= f"../upload/video/outputfile.mp4",download_name=yt.title+".mp4", as_attachment=True)
    return redirect("/")


@app.route('/convert/mp3',methods=['GET','POST'])
def convertmp3():
    if request.method == "POST":
        link = request.form['link']
        flash("Converting Video Please Wait .....")
        yt = YouTube(link)
        yd = yt.streams.get_audio_only()
        yd.download(filename= "./upload/audio/outputfile.mp3")
        flash("Audio Converted Successfully")
        return send_file(path_or_file= f"../upload/audio/outputfile.mp3",download_name=yt.title+".mp3", as_attachment=True)
    return redirect("/")