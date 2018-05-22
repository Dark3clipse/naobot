import nao_nocv

import nao_nocv as nao
import time
#from naoqi import ALProxy
from naoqi import ALModule
import time
from getch import getch
import random

if __name__ == "__main__":
    global asr
    global myIP
    global PORT
    global memProxy
    global faceProxy

    #myIP="10.0.0.221"
    myIP="192.168.0.115"
    PORT=9559
    max_count=30

    nao.InitProxy(myIP,[0])
    asr=nao.speechProxy
    memProxy=nao.memoryProxy
    faceProxy=nao.faceProxy
    tts=nao.tts
##    while True:
##        l=tts.getAvailableLanguages()
##        s=raw_input("Which language do you want "+ str(l)+"? ")
##        if s in l:
##            lang=s
##            break
    lang="Dutch"
 #   print "Setting language to "+lang
    tts.setLanguage(lang)

    nao.InitTrack()
    nao.InitPose()
#    nao.InitSonar()
    time.sleep(3)

    nao.MoveHead(-0.3,-0.5)
    time.sleep(1)
    nao.Say("Hallo mevrouw Driesen, heb je je zuurstof al gecontroleerd.")
 #   nao.RunMovement('pointing_watch2.py')
    time.sleep(0.1)
    nao.RunLED("QuestionLed_3.csv")
    nao.ALTrack(1)
    
    raw_input('press enter to continue ...')
    nao.ALTrack(0)
    nao.Crouch()
        

            
