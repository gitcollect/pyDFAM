import util.coord_extractor, util.methodcall_extractor
import signal, sys, time, os, DB
from datetime import datetime

lastUsrId = DB.getLastUserId()[0]

def main():
    
    startTime = 0
    endTime = 0
    elapsedTime = 0

    def signal_handler(signal, frame):
          
        def cleanUp():
            if lastUsrId is None:
                lastUsrId = 0
            lastUsrId += 1

            endTime = datetime.now()
            elapsedTime = str(endTime - startTime)
            DB.writeUserInfo(lastUsrId, elapsedTime)
            os.popen("rm *.txt")
            sys.exit(1)
        
        util.methodcall_extractor.pullLogFile()

        time.sleep(7)
        
        util.methodcall_extractor.writeMethodCall(lastUsrId)
        
        cleanUp()


    startTime = datetime.now()
    
    util.coord_extractor.writeCOORD()

    signal.signal(signal.SIGINT, signal_handler)
    
    while(True):
        pass

main()
