#! /usr/bin/env python

import os, transition, db


fileName = "mylog.txt"

def pullLogFile():
    os.popen4("adb pull /data/" + fileName)

def parse(line):
    
    try:
        fragments = line.split("\t")
        timestamp = fragments[0]
        className = fragments[2].replace("class ", "")
        touchEvent = fragments[4]
        return transition.Transition(src=None, dst=None, timestamp=timestamp, className=className, touchEvent=touchEvent)

    except IndexError:
        pass

def getTransitions():
    transtions = list()
    f = open("./" + fileName, "r")
    
    lines = f.readlines()

    for idx in range(len(lines)-2):
        t = parse(lines[idx+1])
        transtions.append(t)

    return transtions

def writeMethodCall():
    for transition in getTransitions():
        if transition is not None:
            db.writeMethodCall(transition)


