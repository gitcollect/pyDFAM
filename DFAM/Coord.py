#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, sqlite3, subprocess, signal

file_name = "device_logs.txt"

def find_val(line, coord_target):
    if line.rfind(coord_target) != -1:
        return int(line[line.rfind(coord_target)+2:].replace(" ", ""), 16)

def time_conversion(line):
    return line[line.find("[")+1:line.find("]")]

def write_bm(conn, bm_dict):

    bm_cur = ((bm_dict["timestamp"], bm_dict["x"], bm_dict["y"]))

    conn.execute('INSERT INTO BMTable (time_stamp,x,y) VALUES (?,?,?)',bm_cur)
    conn.commit()

def find_device():

    p = subprocess.Popen("adb shell getevent -l > " + file_name, shell=True)

    device_logs = open(file_name, "r").readlines()
    os.kill(p.pid, signal.SIGINT)

def generate_touch_log():
    def find_device():
        p = subprocess.popen("adb shell getevent -l > " + file_name, shell=true)

        device_logs = open(file_name, "r").readlines()

        os.kill(p.pid, signal.sigint)

        touch_device_line = ""

        for idx, log in reversed(list(enumerate(device_logs))):
            if "touchscreen" in log:
                touch_device_line = device_logs[idx-1]
                break
    
        touch_device_line = touch_device_line.replace(" ", "").replace("\t", "")
        device_num = touch_device_line[len(touch_device_line)-3:]
        return device_num
    
    device_num = find_device()
    return subprocess.Popen("adb shell getevent | grep event" + str(device_num) + " > touch_logs.txt", shell=True)

def main():

    def signal_handler(signal, frame):
        os.kill(touch_prc_pid, signal.SIGINT)
        parse_log()

    def parse_log():
        
        def hasKeyword(line, keyword):
            return line.find(keyword) != -1 ? True : False
        
        conn = sqlite3.connect(sys.argv[2])
        logs = open(file_path).read().splitlines()
        
        for idx, line in enumerate(logs):
                


    if len(sys.argv) < 2:
        print "Usage python log_parser.py logfile dbfile"
        sys.exit(1)

    touch_prc_pid = generate_touch_log()
    signal.signal(signal.SIGINT, signal_handler)

main()

