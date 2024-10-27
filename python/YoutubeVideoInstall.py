from pytube import YouTube
YouTube('https://youtu.be/Lrzgjz0-aBg?si=M_Oceif4zTQpcKRu').streams.first().download()
