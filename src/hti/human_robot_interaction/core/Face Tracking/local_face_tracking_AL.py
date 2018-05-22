import nao
import time
#import msvcrt

from naoqi import ALProxy
from naoqi import ALModule
import time
from getch import getch

def InitSpeech(wordList=["yes","no","hello NAO","goodbye NAO"]):
    global asr
    global memProxy
    global myIP
    global PORT
    
    asr = ALProxy("ALSpeechRecognition",myIP,PORT) #IP = address of your robot
    
#Before starting the ASR engine, you must set the language of the speech recognition system. The list of the installed languages can be obtained through the getAvailableLanguages method.

    asr.setLanguage("English")

    # To set the words that should be recognized, use the setWordListAsVocabulary method.

    print(wordList)
    asr.setWordListAsVocabulary(wordList)

    # create proxy on ALMemory
    memProxy = ALProxy("ALMemory",myIP,PORT)
    print "Init speech done."
    
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



if __name__ == "__main__":
    global asr
    global myIP
    global PORT
    global memProxy


myIP="192.168.0.115"
PORT=9559
myWordList=["yes","no","okay", "goodbye","hello","how are you","I'm fine","horrible","great"]

nao.InitProxy(myIP,[0])
nao.InitTrack()
nao.ALTrack(1)
tts = ALProxy("ALTextToSpeech", myIP, PORT)
InitSpeech(myWordList)

count=0
i=0
try:
    while i<10000:
        location, detected = nao.ALFacePosition()
        print location, detected
        i=i+1
        if detected:
            nao.EyeLED([0,255,0])
            if count>200:
                nao.Say("Hello, how are you?",False)
                print location
                time.sleep(0.2)
                asr.subscribe("MyModule")
                memProxy.insertData("WordRecognized",[])
                
                for i in range(0,300):
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
                            asr.unsubscribe("MyModule")
                            tts.say("You said: "+result[0]+".")
                            time.sleep(0.2)
                            break
                            #asr.subscribe("MyModule")
                    time.sleep(0.2)
                #asr.unsubscribe("MyModule")
                count=0
            else:
                count=count+1
            
        else:
            nao.EyeLED([0,0,0])
    asr.unsubscribe("MyModule")
    nao.EyeLED([0,0,0])
    nao.ALTrack(0)
    nao.EndTrack()
                

except:
    print "exception"

finally:
    print "finally ..."
    asr.unsubscribe("MyModule")
    nao.EyeLED([0,0,0])
    nao.ALTrack(0)
    nao.EndTrack()
    
    
