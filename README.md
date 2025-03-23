# Flask YouTube Downloader

A Flask-based web application to download videos from a user-specified URL. The application uses `yt-dlp` to manage video downloads and provides a simple interface to monitor download speed and ETA.

---

## Features

- **Video Download**: Enter a URL (for example, from YouTube) and download the video directly in your browser.
- **Real-time Monitoring**: Displays download speed and ETA while downloading.
- **Multiple Format Support**: Download videos in MP4 format with the best quality available.

---

## Prerequisites

Before running the project, make sure you have installed:

- **Python 3.x**: The programming language used for the backend.
- **Flask**: A lightweight web framework for Python.
- **yt-dlp**: A library to download videos from platforms such as YouTube.
- **pip**: Python's package manager for installing dependencies.

---

## Download the project 

1. **Clone the repository** 

   Open the terminal and run:
   ```bash 
   git clone https://github.com/RykerWilder/yt-downloader.git
   ```
   ```bash
   cd yt-downloader
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```
   ```bash
   pip install yt-dlp
   ```

4. **Run the app**
   ```bash
   python3 main.py
   ```
   or
   ```bash
    flask --app main run
   ```

The application will be available in your browser at 127.0.0.1:5000.