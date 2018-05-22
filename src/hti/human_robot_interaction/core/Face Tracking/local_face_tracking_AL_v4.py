import nao_nocv as nao
import time
#from naoqi import ALProxy
from naoqi import ALModule
import time
from getch import getch

def InitSpeech(wordList=["yes","no","hello NAO","goodbye NAO"]):
    global asr
    global memProxy
    global myIP
    global PORT
    
    #asr = ALProxy("ALSpeechRecognition",myIP,PORT) #IP = address of your robot
    
#Before starting the ASR engine, you must set the language of the speech recognition system. The list of the installed languages can be obtained through the getAvailableLanguages method.

    asr.setLanguage("English")

    # To set the words that should be recognized, use the setWordListAsVocabulary method.

    print(wordList)
    asr.setWordListAsVocabulary(wordList)

    
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


    myIP="192.168.0.115"
    PORT=9559
    myWordList=["yes","no","okay", "goodbye","hello","how are you","I'm fine","horrible","great"]

    nao.InitProxy(myIP,[0])
    asr=nao.speechProxy
    memProxy=nao.memoryProxy
    faceProxy=nao.faceProxy
    tts=nao.tts

    nao.InitTrack()
    nao.ALTrack(1)

    InitSpeech(myWordList)
    InitFaceDetection()

    # Subscribe to the ALFaceDetection proxy
    # This means that the module will write in ALMemory with
    # the given period below
    period = 500
    faceProxy.subscribe("Test_Face", period, 0.0 )
    tts.say("Look at me")
    count=0
    i=0
    try:
        while 1:
            location, detected = DetectFace()
            #print location, detected
            i=i+1
            if detected:
                nao.EyeLED([0,255,0])
                if count>50:
                    nao.Say("Hello, how are you?",False)
                    print location
                    time.sleep(0.2)
                    asr.subscribe("MyModule")
                    memProxy.insertData("WordRecognized",[])
                    
                    for j in range(0,300):
                        result=DetectSpeech()
                        if len(result)>0:
                            print result
                            if result[0]==myWordList[0]:
                                print myWordList[0]+" recognized."
                            if result[0]==myWordList[1]:
                                print myWordList[1]+" recognized."
                            if result[0]==myWordList[2]:
                                print myWordList[2]+" recognized."
                                break
                            if result[0]==myWordList[3]:
                                print myWordList[3]+" recognized."
                            if result[0]==myWordList[4]:
                                print myWordList[4]+" recognized."
                            if result[0]==myWordList[5]:
                                print myWordList[5]+" recognized."
                            if result[0]==myWordList[6]:
                                print myWordList[6]+" recognized."
                            if result[0]==myWordList[7]:
                                print myWordList[7]+" recognized."
                            if result[0]==myWordList[8]:
                                print myWordList[7]+" recognized."
                            if result[0]=='':
                                print "I did not understand."
                            else:
                                #asr.unsubscribe("MyModule")
                                tts.say("You said: "+result[0]+".")
                                time.sleep(0.2)
                                break
                                #asr.subscribe("MyModule")
                        time.sleep(0.2)
                    asr.unsubscribe("MyModule")
                    count=0
                else:
                    count=count+1
                
            else:
                nao.EyeLED([0,0,0])                    

    except Exception, e:
        print "exception ", e

    finally:
        print "finally ..."
        faceProxy.unsubscribe("Test_Face")
        #asr.unsubscribe("MyModule")
        nao.EyeLED([0,0,0])
        nao.ALTrack(0)
        nao.EndTrack()
        
        
