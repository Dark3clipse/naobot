import nao_nocv as nao
import time
#from naoqi import ALProxy
from naoqi import ALModule
import time
from getch import getch
import random

def InitSpeech(wordList=["ja","nee","hallo","Nao","dag", "tot ziens","hoe gaat het?", "hoe heet jij?"]):
    global asr
    global memProxy
    global myIP
    global PORT
    global lang
    
    #asr = ALProxy("ALSpeechRecognition",myIP,PORT) #IP = address of your robot
    
#Before starting the ASR engine, you must set the language of the speech recognition system. The list of the installed languages can be obtained through the getAvailableLanguages method.

#    lang=asr.getAvailableLanguages()
#    print lang
    asr.setLanguage(lang)

    # To set the words that should be recognized, use the setWordListAsVocabulary method.

    print(wordList)
    asr.setVocabulary(wordList,True)

    
def DetectSpeech():
    global memProxy
    
    try:
        #getData
        result=memProxy.getData("WordRecognized")
        if len(result)>1:
            memProxy.insertData("WordRecognized",[])
            return result

    except RuntimeError,e:
      # catch exception
      print "error getting data", e

    return result

class mySpeechModule(ALModule):
    """python class mySpeechModule test auto documentation"""

    def mySpeechCallBack(self, strVarName, value, message):
        """callback when data change"""
        print "Event is raised and callback is called by ALMemory"
        print value
        print "datachanged", strVarName, " ", value, " ", strMessage

def InitFaceDetection():
    global faceProxy
    global myIP
    global PORT

    # Create a proxy to ALFaceDetection
    try:
      #faceProxy = ALProxy("ALFaceDetection", myIP, PORT)
        pass
     
    except Exception, e:
        print "Error when creating face detection proxy:"
        print str(e)
        exit(1)

def DetectFace():
### A simple loop that reads the memValue and checks whether faces are detected.
    global memProxy
    

#    time.sleep(0.5)
    val = memProxy.getData("FaceDetected", 0)

  # Check whether we got a valid output.
    if(val and isinstance(val, list) and len(val) >= 2):

        # We detected faces !
        # For each face, we can read its shape info and ID.

        # First Field = TimeStamp.
        timeStamp = val[0]

        # Second Field = array of face_Info's.
        faceInfoArray = val[1]

        try:
            
          # Browse the faceInfoArray to get info on each detected face.
            for j in range( len(faceInfoArray)-1 ):
                faceInfo = faceInfoArray[j]

                # First Field = Shape info.
                faceShapeInfo = faceInfo[0]

                # Second Field = Extra info (empty for now).
                faceExtraInfo = faceInfo[1]

                print "  alpha %.3f - beta %.3f" % (faceShapeInfo[1], faceShapeInfo[2])
                print "  width %.3f - height %.3f" % (faceShapeInfo[3], faceShapeInfo[4])

            return [faceShapeInfo[1], faceShapeInfo[2]], True

        except Exception, e:
            print "faces detected, but it seems getData is invalid. ALValue ="
            print val
            print "Error msg %s" % (str(e))
    else:
        #print "No face detected"
        return [], False


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
    nao.ALTrack(1)

    if lang=="Dutch":
        myWordList=["Hallo","Nao","goed", "redelijk", "slecht","dag", "tot ziens","hoe gaat het?", "hoe heet jij?"]
        s0=["Hallo, ik ben Nao"]
        s1=["Hallo", "Hoe gaat het?","Ik ben Nao, hoe gaat het"]
        s2=["", "","Wat zeg je?","Ik verstond het niet."]
        s3=["Jij zei"]
        s4=["Mooi!", "Fijn om te horen.", "Met mij ook!"]
        s5=["Dat is niet zo best.","Kan ik iets voor je doen?","Dat is jammer."]
    elif lang=="English":
        myWordList=["Nao", "goodbye","hello","how are you","I'm fine","great", "not good", "bad","horrible"]
        s0=["Hi, I am Nao"]
        s1=["Hello", "How are you?","I am Nao, how are you?","What's your name?","Who are you?","What did you say?"]
        s2=["", "","Say again?","I did not understand."]
        s3=["You said"]

    InitSpeech(myWordList)
    InitFaceDetection()

    # Subscribe to the ALFaceDetection proxy
    # This means that the module will write in ALMemory with
    # the given period below
    period = 500
    faceProxy.subscribe("Test_Face", period, 0.0 )
    tts.say(random.choice(s0))
    count=0
    i=0
    try:
        while 1:
            location, detected = DetectFace()
            #print location, detected
            i=i+1
            if detected:
                nao.EyeLED([0,255,0])
                if count>max_count:
 #                   nao.Say(random.choice(s1),False)
                    print location
                    time.sleep(0.2)
                    asr.subscribe("MyModule")
                    memProxy.insertData("WordRecognized",[])
                    
                    for j in range(0,300):
                        result=DetectSpeech()
                        if len(result)>0:
                            print result
                            if result[0] in myWordList:
                                print result[0] + " recognized."
                                if result[0]=='goed':
#                                    tts.say(random.choice(s4))
                                    pass
                                elif result[0]=='slecht':
                                    pass
#                                    tts.say(random.choice(s5))
                                elif result[0]== "hoe heet jij?":
#                                    tts.say("Ik heet Nao.")
                                    pass
                                elif result[0]=='tot ziens':
                                    tts.say("Tot ziens!")
                                    break
                                    

                            if result[0]=='':
 #                              tts.say(random.choice(s2)+' '+result[0]+".")
                               print "I did not understand."
                            else:
                                #asr.unsubscribe("MyModule")
 #                               tts.say(random.choice(s3)+': '+result[0]+".")
                                time.sleep(0.2)
                                break
                                #asr.subscribe("MyModule")
                        time.sleep(0.2)
                    asr.unsubscribe("MyModule")
                    count=0
                else:
                    count=count+1
                
            else:
                nao.EyeLED([255,255,255])                    

    except Exception, e:
        print "exception ", e

    finally:
        print "finally ..."
        time.sleep(1)
        nao.EyeLED([0,0,0])
        nao.ALTrack(0)
        nao.EndTrack()
        faceProxy.unsubscribe("Test_Face")
        try:
            asr.unsubscribe("MyModule")
        except:
            pass
        time.sleep(1)
        
        
