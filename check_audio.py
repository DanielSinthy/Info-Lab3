import tkinter as tk
from tkinter import filedialog
import librosa

root = tk.Tk()

tempo_label = tk.Label(root, text="Tempo: ")
tempo_label.pack()

def analyze_audio(file_path):
    # Load audio file
    y, sr = librosa.load(file_path)

    # Get tempo (BPM)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    # Display tempo
    tempo_label.config(text="Tempo: {:.2f} BPM".format(tempo))

def select_file():
    file_path = filedialog.askopenfilename()
    analyze_audio(file_path)
   

