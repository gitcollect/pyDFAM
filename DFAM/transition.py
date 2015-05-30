#! /usr/bin/env python

class Transition(object):
    timestamp = -1
    touchEvent = ""
    methodName = ""
    src = None
    dst = None

    def __init__(self, src, dst, timestamp, touchEvent, methodName):
        self.src = src
        self.dst = dst
        self.timestamp = timestamp
        self.touchEvent = touchEvent
        self.methodName = methodName

    def toStr(self):
        print "timestamp : " + self.timestamp + " methodName : " + self.methodName + " touchEvent : " + self.touchEvent

