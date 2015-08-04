#! /usr/bin/env python

import os, model.transition, DB

fileName = "mylog.txt"

def pullLogFile():
    os.popen4("aDB pull /data/" + fileName)

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
            DB.writeMethodCall(transition)
            seq_id = DB.getLastSeqId()[0]
            DB.writeBM(usr_id, seq_id)
