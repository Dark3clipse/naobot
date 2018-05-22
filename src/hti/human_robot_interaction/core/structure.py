'''
Created on 24 Apr 2018

@author: Sophia
'''

import nao_nocv_2_0 as nao
import pykalman as klib
import numpy as np
from cmath import *
import time

#initialize the robot
nao.InitProxy("127.0.0.1", [])
nao.InitPose(.5, .8)

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

while(True):
    if state == STATE_SCANFACE:
        #Start the face detection
        [detected, timestamp, facePosition] = nao.DetectFace(True, 100)
        if detected == True:
            print("Face detected at t="+timestamp+", position"+facePosition)
            
            #nao.MoveHead(yaw_val, pitch_val, isAbsolute, post, timeLists)
            #nav_position = 
            #nav_angle = 
            nav_personal = True
            state = STATE_NAVIGATE
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