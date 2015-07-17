#! /usr/bin/env python

import os, transition, db

fileName = "mylog.txt"

def pullLogFile():
    os.popen4("adb pull /data/" + fileName)

def parse(line):
    
    try:
        fragments = line.split("\t")
        timestamp = fragments[0]
        screen = fragments[1]
        className = fragments[2].replace("class ", "")
        objectId = fragments[3]
        touchEvent = fragments[4]

        return transition.Transition(src=None, dst=None, timestamp=timestamp, className=className, touchEvent=touchEvent, screen=screen, objectId=objectId)

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


def writeMethodCall(usr_id):
    for transition in getTransitions():
        if transition is not None:
            db.writeMethodCall(transition)
            seq_id = db.getLastSeqId()[0]
            db.writeBM(usr_id, seq_id)
