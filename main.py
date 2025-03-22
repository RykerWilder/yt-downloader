from flask import Flask, render_template, request, redirect, url_for
from yt_dlp import YoutubeDL

app = Flask(__name__)

# Cartella dove verranno salvati i video
output_folder = "./videos"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    # Ottieni l'URL dal modulo HTML
    link = request.form["url"]

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', 
        'merge_output_format': 'mp4', 
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        return "<h1>Download completato!</h1>"
    except Exception as e:
        return f"<h1>Errore durante il download: {e}</h1>"

# if __name__ == "__main__":
#     app.run(debug=True)