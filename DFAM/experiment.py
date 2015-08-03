import coord_extractor, methodcall_extractor
import signal, sys, time, os, DB
from datetime import datetime

def main():
    
    startTime = 0
    endTime = 0
    elapsedTime = 0

    def signal_handler(signal, frame):
          
        def cleanUp():
            lastUsrId = DB.getLastUserId()[0]
            if lastUsrId is None:
                lastUsrId = 0
            lastUsrId += 1

            endTime = datetime.now()
            elapsedTime = str(endTime - startTime)
            DB.writeUserInfo(lastUsrId, elapsedTime)
            os.popen("rm *.txt")
            sys.exit(1)
        
        methodcall_extractor.pullLogFile()

        time.sleep(7)
        
        lastUsrId = DB.getLastUserId()[0]
        methodcall_extractor.writeMethodCall(lastUsrId)
        
        cleanUp()


    startTime = datetime.now()
    
    coord_extractor.writeCOORD()

    signal.signal(signal.SIGINT, signal_handler)
    
    while(True):
        pass

main()
