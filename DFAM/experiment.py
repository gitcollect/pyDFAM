import coord_extractor, methodcall_extractor
import signal, sys, time, os, db
from datetime import datetime

def main():
    
    startTime = 0
    endTime = 0
    elapsedTime = 0

    def signal_handler(signal, frame):
          
        def cleanUp():
            lastUsrId = db.getLastUserId()[0]
            if lastUsrId is None:
                lastUsrId = 1
            lastUsrId += 1

            endTime = datetime.now()
            elapsedTime = str(endTime - startTime)
            db.writeUserInfo(lastUsrId, elapsedTime)
            os.popen("rm *.txt")
            sys.exit(1)

        methodcall_extractor.pullLogFile()
        coord_extractor.pullLogFile()

        time.sleep(7)
        
        lastUsrId = db.getLastUserId()[0]
        
        if lastUsrId is None:
            lastUsrId = 1
        
        methodcall_extractor.writeMethodCall(lastUsrId)
        coord_extractor.writeCOORD()
        
        cleanUp()


    startTime = datetime.now()

    coord_extractor.generateLog()

    signal.signal(signal.SIGINT, signal_handler)
    
    while(True):
        pass

main()
