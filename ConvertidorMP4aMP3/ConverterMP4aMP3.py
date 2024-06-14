from moviepy.editor import *

# Carga el archivo de video .mp4
video = VideoFileClip("/Users/deibysr/Movies/MeditacionRecorte1.mp4")

# Extrae el audio del video
audio = video.audio

# Guarda el audio extraído en formato .mp3
audio.write_audiofile("/Users/deibysr/Movies/MeditacionRecorte1.mp3")
