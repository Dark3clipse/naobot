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

    sensorsProxy = nao.naoqi.ALProxy("ALSensors",myIP,PORT)

    sensorsProxy.run()

    while 1:
        val1=memProxy.getData('Device/SubDeviceList/LHand/Touch/Back/Sensor/Value')
        val2=memProxy.getData('Device/SubDeviceList/LHand/Touch/Left/Sensor/Value')
        val3=memProxy.getData('Device/SubDeviceList/LHand/Touch/Right/Sensor/Value')
        print val1,val2,val3
        time.sleep(0.1)

        

            
