'''
Created on 24 Apr 2018

@author: Sophia
'''

import nao_nocv_2_0 as nao
import pykalman as klib
import numpy as np
from cmath import *
import time

nao.InitProxy("127.0.0.1")
nao.InitSonar(flag = True)

# state_space = [x, y, theta]
def f1(theta, psi):
    return -sin(theta - psi)

def f2(theta, psi, var, beta, dobs):
    return (theta - psi) * exp(-(theta-psi)^2/(2*var)) * exp(-dobs / beta)

def f3(theta, theta_final, dt):
    return -exp(-dt)*sin(theta-theta_final)

def calcDt(x, y, xtar, ytar):
    return sqrt((xtar-x)^2 + (ytar-y)^2)

xtar = 2
ytar = 0
theta_final = 30
w = 1

#kf = klib.KalmanFilter(initial_state_mean=0, n_dim_obs=1)

sonarMeasure = np.empty([0,2])
while(True):
    newMeasure = np.matrix(nao.ReadSonar())
    sonarMeasure = np.append(sonarMeasure, newMeasure, axis=0)
    
    theta = 0
    x = 0
    y = 0
    
    dt = np.real(w * f3(theta, theta_final, calcDt(x, y, xtar, ytar))) # w(t)
    print(dt)
    nao.Walk(1.0, 0.0, dt, post=True)
    
    time.sleep(.1)
    
print sonarMeasure