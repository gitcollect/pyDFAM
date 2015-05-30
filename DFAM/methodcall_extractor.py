#! /usr/bin/env python

import subprocess, transition, db


fileName = "mylog.txt"

def pullLogFile():
    subprocess.Popen("adb pull /data/" + fileName, shell=True)   

def parse(line):
    fragments = line.split("\t")
    timestamp = fragments[0]
    methodName = fragments[2].replace("class ", "")
    touchEvent = fragments[4]

    return transition.Transition(src=None, dst=None, timestamp=timestamp, methodName=methodName, touchEvent=touchEvent)

def getTransitions():
    transtions = list()
    pullLogFile()
    f = open("./" + fileName, "r")
    
    lines = f.readlines()

    for idx in range(len(lines)-2):
        t = parse(lines[idx+1])
        transtions.append(t)

    return transtions

def writeMethodCall():
    for transition in getTransitions():
        db.writeMethodCall(transition)


