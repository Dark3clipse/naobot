import math
from math import exp
from math import sin

degree = math.pi/180.0 # radians per degree

def FTarget(target_angle):

    #do something useful here
    Ftar= - sin( - target_angle)
    return Ftar

def FObstacle(obs_distance, obs_angle):
    too_far = 2 #m
    too_close = 0.28

    if obs_distance < too_far:
        #do something useful here
        #sigma and beta unknown
        Fobs = exp( - (obs_angle)**2) * ( - obs_angle) * exp( -obs_distance)
    else:
        Fobs=0
    return Fobs

def FStochastic(sonar_distance_left, sonar_distance_right):
    #noise force
    if sonar_distance_left == sonar_distance_right > 2:
        Fstoch = 0.5 #need adjustment
    else:
        Fstoch = 0
    return Fstoch

def FOrienting( target_distance, target_angle):
    #do something useful here
    #alingment force
    Forient= - exp( -target_distance) * sin( -target_angle)
    return Forient

def compute_velocity(sonar_distance_left, sonar_distance_right):
    max_velocity = 1.0
    max_distance = 0.7 #m
    min_distance = 0.3 #m

    if sonar_distance_left > max_distance and sonar_distance_right > max_distance:
        velocity = max_velocity
    elif sonar_distance_left < min_distance or sonar_distance_right < min_distance:
        velocity = 0.0
    elif sonar_distance_left < sonar_distance_right:
        velocity = max_velocity*sonar_distance_left / max_distance
    else:
        velocity = max_velocity*sonar_distance_right / max_distance
        
    return velocity

def compute_turnrate(target_dist, target_angle, sonar_distance_left, sonar_distance_right):
    max_turnrate = 0.349 #rad/s

    delta_t = 0.2 # may need adjustment!
    sonar_angle_left = 30 * degree #degree is a constant; thus sonar angle is also constant
    sonar_angle_right = -30 * degree
    
    Fobs_left = FObstacle(sonar_distance_left, sonar_angle_left)
    Fobs_right = FObstacle(sonar_distance_right, sonar_angle_right)

    FTotal = FTarget( target_angle) + Fobs_left + Fobs_right + FOrienting( target_dist, target_angle) + FStochastic(sonar_distance_left, sonar_distance_right)

    # turnrate: d phi(t) / dt = sum( forces ) 
    turnrate =  FTotal*delta_t
    
    #normalise turnrate value
    if turnrate > max_turnrate:
        turnrate = 1.0
    else:
        turnrate = turnrate/max_turnrate

    return turnrate

if __name__=="__main__":
    pass
