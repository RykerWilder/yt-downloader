from flask import Flask, request, send_file, render_template, after_this_request
from yt_dlp import YoutubeDL
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    # Ottieni l'URL dal modulo HTML
    link = request.form["url"]

    # Opzioni per yt-dlp
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', 
        'merge_output_format': 'mp4', 
        'outtmpl': '%(title)s.%(ext)s',  # Salva il video nella directory corrente
    }

    try:
        # Scarica il video
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            video_title = info_dict['title']
            video_filename = f"{video_title}.mp4"

        # Funzione per eliminare il file dopo il download
        @after_this_request
        def remove_file(response):
            try:
                os.remove(video_filename)
            except Exception as e:
                app.logger.error(f"Errore durante l'eliminazione del file: {e}")
            return response

        # Restituisci il file come risposta
        return send_file(
            video_filename,
            as_attachment=True,
            download_name=video_filename,
            mimetype="video/mp4"
        )
    except Exception as e:
        return f"<h1>Errore durante il download: {e}</h1>"

if __name__ == "__main__":
    app.run(debug=True)