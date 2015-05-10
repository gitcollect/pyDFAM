#! /usr/bin/env python

fileName = "mylog.txt"

def pullLogFile():
    os.popen("adb pull /data/" + fileName)

def parse(line):
    fragments = line.split("\t")
    
    timestamp = fragments[0]
    methodName = fragments[2]
    touchEvent = fragments[4]

    return Transition(timestamp=timestamp, methodName=methodName, touchEvent=touchEvent)

def getTransitions():
    transtions = []
    pullLogFile()
    f = open(fileName, "r")
    for line in f.readlines():
        transtions.extend(parse(line))
    
    return transtions
