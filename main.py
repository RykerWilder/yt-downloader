from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    from yt_dlp import YoutubeDL

    link = "" 
    output_folder = "./videos" 

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', 
        'merge_output_format': 'mp4', 
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        return "<h1>Hello, World!</h1>"