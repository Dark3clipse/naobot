'''
Created on 24 Apr 2018

@author: Sophia
'''

import nao_nocv_2_0 as nao
import pykalman as klib
import numpy as np
from cmath import *
import time
import random
import naoqi

#initialize the robot
myIP = "192.168.0.115"
nao.InitProxy(myIP, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

#possible states
STATE_SCANFACE = 0
STATE_NAVIGATE = 1
STATE_FIRSTCONTACT_ATTENTION = 2
STATE_FIRSTCONTACT_SENTENCE = 3
STATE_FINDREASON = 4
STATE_ARRIVEDATDESTINATION = 5

#holds the current state
state = STATE_SCANFACE;

#general constants
c_personal_space_distance = 1

#global variables
nav_position = np.array([0, 0]) #position to navigate to
nav_angle = 0
nav_personal = False
waiting_area = 0

nao.Say("Program Started")

while(True):
    if state == STATE_SCANFACE:
        #Start the face detection
        print("STATE: scan face")
        try:
            nao.Crouch(.8)
            nao.InitTrack()
            nao.InitSpeech(wordList=["yes","no"], the_language="English", wordSpotting=False)
        
            track_count = 0
            count=0
            said = False
            while(track_count < 1500 and state == STATE_SCANFACE):
                location, detected = nao.ALFacePosition()
                if detected:
                    nao.EyeLED([0,255,0])
                    nao.Track(location, detected, 5, 0.02)
                    if count>50 and said == False:
                        txt = ["Do you need any assistance?", "Would you like me to assist you?", "Would you like assistance?", "Do you need any help?"]
                        nao.Say(txt[random.randint(0, 3)])
                        speech_count = 0
                        nao.InitSoundDetection(True)
                        nao.EyeLED([255,128,0])
                        asr = naoqi.ALProxy("ALSpeechRecognition", myIP, 9559)
                        asr.subscribe("REC")
                        while(speech_count < 500):
                            
                            result = nao.DetectSpeech()
                            print(result)
                            if (len(result) > 0):
                                if (result[0] == "yes"):
                                    nao.Say("Please follow me.")
                                    state = STATE_FINDREASON
                                    break
                                elif (result[0] == "no"):
                                    nao.Say("Help yourself then")
                                    break
                                else:
                                    nao.Say("I could not hear you.")
                            speech_count+=1
                        nao.InitSoundDetection(False)
                        asr.unsubscribe("REC")
                        if (speech_count < 500):
                            said = True
                        count=0
                    else:
                        count=count+1
                else:
                    nao.EyeLED([255,0,0])
                    #nao.Track([0, 0], detected,5,0.02)
                track_count += 1
                
        except Exception, e:
            print "exception ", e
            nao.Say("Your program is malfunctioning.")

        finally:
            nao.EndTrack()
            nao.EyeLED([0,0,255])
            nao.MoveHead(0, 0, False)
            nao.Say("Back to sleep")
            break
        pass
    
    elif state == STATE_NAVIGATE:
        
        pass
    
    elif state == STATE_FIRSTCONTACT_ATTENTION:
        
        pass
    
    elif state == STATE_FIRSTCONTACT_SENTENCE:
        
        pass
    
    elif state == STATE_FINDREASON:
        
        pass
    
    elif state == STATE_ARRIVEDATDESTINATION:
        
        pass