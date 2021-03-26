from pygame import mixer
from time import time
from datetime import datetime


def musiconloop( file , stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_from_user=input()
        if input_from_user==stopper:
            mixer.music.stop()
            break
        elif input_from_user=="quit":
            global bool
            bool=False
            break

def log(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__=="__main__":
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60
    bool=True
    while bool:
        if time() - init_water > watersecs:
            print("Water drinking time. Enter 'drank' to stop the alarm or 'quit' to end the program." )
            musiconloop('water.ogg',"drank")
            init_water=time()
            log("Drank water at ")
        if time() - init_eyes > eyessecs:
            print("Rub your eyes. Enter 'rubbed' to stop the alarm or 'quit' to end the program." )
            musiconloop('eyes.ogg',"rubbed")
            init_eyes=time()
            log("Rubbed eyes at ")
        if time() - init_exercise > exsecs:
            print("Exercise time. Enter 'done' to stop the alarm or 'quit' to end the program." )
            musiconloop('exercise.ogg',"done")
            init_exercise=time()
            log("Did exercise at ")







