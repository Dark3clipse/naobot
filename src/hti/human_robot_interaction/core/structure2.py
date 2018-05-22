'''
Created on 24 Apr 2018

@author: Sophia
'''

import nao_nocv_2_0 as nao
import naoqi
#import pykalman as klib
#import numpy as np
#from cmath import *
import time

#initialize the robot
nao.InitProxy("127.0.0.1")

#possible states
STATE_SCANFACE = 0
STATE_NAVIGATE = 1
STATE_FIRSTCONTACT_ATTENTION = 2
STATE_FIRSTCONTACT_SENTENCE = 3
STATE_FINDREASON = 4
STATE_ARRIVEDATDESTINATION = 5

#holds the current state
state = STATE_FIRSTCONTACT_ATTENTION;

#general constants
c_personal_space_distance = 1


#global variables
#nav_position = np.array([0, 0]) #position to navigate to
nav_angle = 0
nav_personal = False
waiting_area = 0
go = True

def getAttention():
    nao.InitPose()
    nao.Say("Hello")
    nao.RunMovement("/gestures/Welcoming.py")
    #nao.Crouch()
    #time.sleep(1)

def firstContact():
    nao.Say("Can I help you?")
    answer = detectSpeech()
    if answer == "yes":
        state = STATE_FINDREASON
    elif:
        #state = STATE_NAVIGATE(start position)

def detectSpeech():
    #blablabla

while(go == True):
    if state == STATE_SCANFACE:
        
        pass
    
    elif state == STATE_NAVIGATE:
        
        pass
    
    elif state == STATE_FIRSTCONTACT_ATTENTION:
        getAttention()
        #state_scanface; if face is seen --> state = STATE_FIRSTCONTACT_SENTENCE
        go = False
        pass
    
    elif state == STATE_FIRSTCONTACT_SENTENCE:
        firstContact()
        pass
    
    elif state == STATE_FINDREASON:
        
        pass
    
    elif state == STATE_ARRIVEDATDESTINATION:
        
        pass
