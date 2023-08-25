import os
from mutagen.mp3 import MP3

path = "BAJAJ RBL AUDIO"


def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return(hours, mins, seconds)

total_lenght = 0
for root, dirs, files in os.walk(os.path.abspath(path)):
    for file in files:
        if file.endswith(".mp3"):
            # print(os.path.join(root, file))
            audio = MP3(os.path.join(root, file))
            # print(audio.info.length)
            hours, mins, seconds = convert(audio.info.length)
            string=os.path.join(root, file)
            filename = string[23:10000]
            print(filename)

            # print(str(int(hours)) + ":" +
            #       str(int(mins)) + ":" + str(int(seconds)))
            
            total_lenght += audio.info.length
            hours, mins, seconds = convert(total_lenght)
            
            # print("Total lenght of all audios"+" - "+str(int(hours)) + ":" +
            #       str(int(mins)) + ":" + str(int(seconds)))