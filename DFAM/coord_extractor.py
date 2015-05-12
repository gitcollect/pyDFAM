#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, sqlite3, subprocess, signal

fileName = "device_logs.txt"

def writeBM(conn, x, y):

    bm_cur = (x, y)
    conn.execute('INSERT INTO SeqTable (x,y) VALUES (?,?)', (x,y))
    conn.commit()

def generateLog():
    return os.popen4("adb shell getevent -lt | grep event0 > " + fileName)

def pullLogFile():
    return os.popen4("adb pull /data/"+fileName)

def main():

    def signal_handler(signal, frame):
        pullLogFile()
        parse()
        sys.exit(1)

    def parse():

        # return decimal value from hex coord string
        def getCOORDvalue(line, idx):
            return int(line[idx+17:].replace(" ", ""), 16)

        conn = sqlite3.connect(sys.argv[1])
        logs = open(fileName).read().splitlines()

        for idx, line in enumerate(logs):
            idx_key = line.rfind("ABS_MT_POSITION_X")

            if idx_key > -1:
                x = getCOORDvalue(logs[idx], idx_key)
                y = getCOORDvalue(logs[idx+1], idx_key)
                writeBM(conn,x,y)

    if len(sys.argv) < 1:
        print "Usage python log_parser.py logfile dbfile"
        sys.exit(1)

    generateLog()
    signal.signal(signal.SIGINT, signal_handler)

    while(True):
        pass


main()
