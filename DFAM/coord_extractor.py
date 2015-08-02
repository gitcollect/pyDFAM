#!/usr/bin/python
# -*- coding: utf-8 -*-

import db, os

fileName = "device_logs.txt"

def generateLog():
    return os.popen4("adb shell getevent -lt | grep event0 > " + fileName)

def pullLogFile():
    return os.popen4("adb pull /data/"+fileName)

def writeCOORD():
        
    def getCOORDvalue(line, idx):
        return int(line[idx+17:].replace(" ", ""), 16)

    logs = open(fileName).read().splitlines()
    
    seq_id = 1

    for log in enumerate(logs, start = 1):
            
        frag = log[1]
            
        idx_key = frag.rfind("ABS_MT_POSITION_X")

        if idx_key > -1:
            try:
                x = getCOORDvalue(frag, idx_key)
                y = getCOORDvalue(logs[int(log[0])], idx_key)
                db.writeCOORD(seq_id, x, y)
            except ValueError:
                pass
            
        isTouchEnd = frag.rfind("ABS_MT_TRACKING_ID")
               
        if isTouchEnd > -1:
            seq_id += 1
