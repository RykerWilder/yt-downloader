from flask import Flask, request, send_file, render_template, jsonify
from yt_dlp import YoutubeDL
import os
import re

app = Flask(__name__)

# Variabile globale per memorizzare lo stato del download
download_status = {
    "speed": "0 B/s",
    "eta": "0s",
    "downloaded_bytes": 0,
    "total_bytes": 0,
}

# Funzione per rimuovere i codici di colore ANSI
def clean_ansi_codes(text):
    """
    Rimuove i codici di colore ANSI da una stringa.
    """
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

# Funzione di callback per il progresso del download
def progress_hook(d):
    global download_status
    if d['status'] == 'downloading':
        download_status["speed"] = clean_ansi_codes(d.get('_speed_str', '0 B/s'))
        download_status["eta"] = clean_ansi_codes(d.get('_eta_str', '0s'))
        download_status["downloaded_bytes"] = d.get('downloaded_bytes', 0)
        download_status["total_bytes"] = d.get('total_bytes', 0)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    global download_status
    # Ottieni l'URL dal modulo HTML
    link = request.form["url"]

    # Opzioni per yt-dlp
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', 
        'merge_output_format': 'mp4', 
        'progress_hooks': [progress_hook],  # Aggiungi l'hook per il progresso
    }

    try:
        # Scarica il video
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            video_title = info_dict['title']
            video_filename = f"{video_title}.mp4"

        # Restituisci il file come risposta
        return send_file(
            video_filename,
            as_attachment=True,
            download_name=video_filename,
            mimetype="video/mp4"
        )
    except Exception as e:
        return f"<h1>Errore durante il download: {e}</h1>"

@app.route("/status")
def status():
    global download_status
    return jsonify(download_status)

if __name__ == "__main__":
    app.run(debug=True)