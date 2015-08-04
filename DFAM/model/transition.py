#! /usr/bin/env python

class Transition(object):
    timestamp = -1
    objectId = ""
    screen =""
    touchEvent = ""
    className = ""
    src = None
    dst = None

    def __init__(self, src, dst, timestamp, objectId, touchEvent, className, screen):
        self.screen = screen
        self.src = src
        self.dst = dst
        self.objectId = objectId
        self.timestamp = timestamp
        self.touchEvent = touchEvent
        self.className = className

    def getCursor(self):
        return (self.timestamp, self.objectId, self.className, self.touchEvent, self.screen)

    def toStr(self):
        print "timestamp : " + self.timestamp + " className : " + self.className + " touchEvent : " + self.touchEvent

