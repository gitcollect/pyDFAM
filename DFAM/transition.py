#! /usr/bin/env python

class Transition(object):
    x = 0
    y = 0
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
