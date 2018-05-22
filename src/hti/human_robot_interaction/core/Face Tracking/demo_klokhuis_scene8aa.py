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
    print "Setting language to "+lang
    tts.setLanguage(lang)

    nao.InitTrack()
    nao.InitPose()
    nao.InitSonar()
    sensorsProxy = nao.naoqi.ALProxy("ALSensors",myIP,PORT)
    time.sleep(3)
    raw_input('press enter to continue ...')
    nao.motionProxy.setAngles("LShoulderPitch",-0.9,0.2)
    nao.motionProxy.openHand("LHand")
    time.sleep(1)
    raw_input('press enter to continue ...')
    nao.motionProxy.setWalkArmsEnabled (False, False)
    time.sleep(1)
    nao.Say("Volg mij maar.")
    time.sleep(2)
    sensorsProxy.run()
    t0=time.time()
    dx=0.5
    dy=0
    dtheta=0
    nao.Move(dx,dy,dtheta)
    while (time.time()-t0)<25:
        if nao.HeadTouch():
            break
        [ls, rs]=nao.ReadSonar()
#        print time.time()-t0,ls,rs
        if ls<0.25 or rs<0.25:
            print "safety stop"
            nao.Move(0.0,0.0,0.0)
            time.sleep(0.1)
            nao.Say("Oeoeps!")
            time.sleep(0.4)
##            t1=time.time()
##            while (time.time()-t1)<1:
##                nao.Move(-0.50,0,0)
##            nao.Move(0.0,0.0,0.0)
##            time.sleep(0.5)
            nao.InitPose()
            time.sleep(0.5)
            break
        if ls<(rs-0.1):
            dx=0.5
            dy=-0.15    
#            dtheta=-0.5
        elif rs<(ls-0.1):
            dx=0.5
            dy=0.15
#            dtheta=+0.5    raw_input('press enter to continue ...')

        elif rs<0.5 and ls<0.5: #slow down
            dx=0.5
            dy=0
            dtheta=0            
        else:
            dx=1
            dy=0
            dtheta=0
#        val=nao.memoryProxy.getData('Device/SubDeviceList/LHand/Touch/Back/Sensor/Value')
#        print val
        nao.Move(dx,dy,dtheta)
        
    nao.Move(0.0,0.0,0.0)
#    time.sleep(1)
##    nao.RunMovement('wave_one.ges')
#    tts.say("Hallo, ik ben Nao.")
 #   nao.ALTrack(1)
    time.sleep(1)
##    while not nao.HeadTouch():
##        s=getch()
##        if s=='q':
##            print 'quitting...'
##            break
##        pass
    raw_input('press enter to continue ...')
#    nao.Say(random.choice(["Ik ben moe.","Ik ga uitrusten."]))
#    nao.RunMovement('wipeforehead.ges')
    time.sleep(1)
    nao.Crouch()
        

            
