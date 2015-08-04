__author__ = 'kyeongwookma'

import subprocess, os
import time

cmd = 'adb shell getevent -lt | grep event0'

def record():
    def getCurrentViewState():
        return os.popen('dump -IS').readlines()

    def writeStateFile(timestamp):
        filePath = './state/' + str(timestamp) + ".txt"
        with open(filePath, 'w') as f:
            f.writelines(getCurrentViewState())
        return filePath

    p = subprocess.Popen(cmd, shell=True, bufsize=64, stdout=subprocess.PIPE)
    for line in iter(p.stdout.readline, ''):
         if line.rfind("ABS_MT_TRACKING_ID") > -1:
             writeStateFile(time.time())


record()
