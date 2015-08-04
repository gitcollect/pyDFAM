#!/usr/bin/python
# -*- coding: utf-8 -*-

import DB, os, subprocess

lastUsrId = str(DB.getLastUserId()[0])

def generateLog():
    cmd = "adb shell getevent -lt | grep event0"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return p.stdout

def writeCOORD():

    def getCOORDvalue(line, idx):
        return int(line[idx+17:].replace(" ", ""), 16)
    
    seq_id = 1

    tmp_x = 0
    tmp_y = 0

    for log in generateLog():
            
        frag = log.rstrip()
        idx_key = frag.rfind("ABS_MT_POSITION_X")

        x = 0
        y = 0

        if idx_key > -1:
            try:
                x = getCOORDvalue(frag, idx_key)
                if x != 0:
                    tmp_x = x
            except ValueError:
                pass
        
        idx_key = frag.rfind("ABS_MT_POSITION_Y")
        
        if idx_key > -1:
            try:
                y = getCOORDvalue(frag, idx_key)
                if y != 0:
                    tmp_y = y
            except ValueError:
                pass
        
        if tmp_x != 0 and tmp_y != 0:
            DB.writeCOORD(seq_id, tmp_x, tmp_y)

        isTouchEnd = frag.rfind("ABS_MT_PRESSURE")
        
        timestamp = frag[frag.find("[")+1:frag.find("]")].replace(" ", "")

        # touch ended
        if isTouchEnd > -1:
            screenshotCmd = "monkeyrunner " + os.getcwd() + "/util/screenshot.py " + lastUsrId + " " + str(timestamp)
            print screenshotCmd
            subprocess.Popen(screenshotCmd, shell=True)
            seq_id += 1
