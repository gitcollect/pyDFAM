#! /usr/bin/env python

class Transition(object):
    timestamp = -1
    touchEvent = ""
    className = ""
    src = None
    dst = None

    def __init__(self, src, dst, timestamp, touchEvent, className):
        self.src = src
        self.dst = dst
        self.timestamp = timestamp
        self.touchEvent = touchEvent
        self.className = className

    def getCursor(self):
        return (self.timestamp, self.className, self.touchEvent)


    def toStr(self):
        print "timestamp : " + self.timestamp + " className : " + self.className + " touchEvent : " + self.touchEvent

