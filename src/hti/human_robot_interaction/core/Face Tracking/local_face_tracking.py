import nao_nocv_2_0 as nao
#import msvcrt

IP = "192.168.0.115"


nao.InitProxy(IP)
nao.InitPose(.5, .8)
nao.InitTrack()
count=0
#try:
while True:
    location, detected = nao.ALFacePosition()
    if detected:
        nao.Track(location,detected,5,0.02)
        nao.EyeLED([0,255,0])
        if count>300:
            nao.Say("Hello, how are you?")
            print location
            count=0
        else:
            count=count+1
        
    else:
        #nao.Track([0,0],False,5,0.04)
        nao.EyeLED([0,0,0])
            

    #    x = msvcrt.getch()
    #    print x
        
#finally:
nao.EndTrack()
