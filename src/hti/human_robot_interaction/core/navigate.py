import behaviour_based_navigation as bn
import math
import nao_nocv_2_0 as nao

def navigate():
    complete = False
    marker_distance = 5  # m; roughly the meaximum detecting distance
    marker_angle = 0 # radians
    marker_id = 0
    min_distance = 0.7 # marker_distance doesn't get lower than 0.6

    while not complete:
        # sonar
        [ sl, sr] = nao.ReadSonar()
        # landmark detection
        #landmark_detected, timestamp, markerinfo = nao.DetectLandMark()
        landmark_detected = False
        if landmark_detected:
            [marker_distance, marker_angle, marker_id] = compute_markerpos( markerinfo)
            # need a code that if landmark is found from InitTrack (headmovement)
            # adjust his body angle
            if marker_distance < min_distance: # the target is reached
                complete = True
        else:
            # if land mark is not found, move his head, and walk forward with obstacle avoidance
            nao.InitTrack()
            marker_distance = 0
            marker_angle = 0
            #print "Target is not found"
            pass

        # Turn rate and velocity
        velocity = bn.compute_velocity( sl, sr) #could be anything, but here: slow down for obstacles
        turn_rate = bn.compute_turnrate( marker_distance, marker_angle, sl, sr,) #turn towards target and the landmark is the target 
        nao.Move( velocity, 0, turn_rate)
        nao.sleep( 0.05) # refresh rate

    # Arrived landmark
    state = 5
    return state

if __name__ == "__main__":
     pass
