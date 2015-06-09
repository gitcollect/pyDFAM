import sqlite3
DBFile = "BadUIDB"

conn = sqlite3.connect(DBFile)

def writeCOORD(seq_id, x, y):
    conn.execute('INSERT INTO COORDTable(seq_id ,x, y) VALUES(?, ?, ?)', (seq_id, x,y))
    conn.commit()

def getLastSeqId():
    return conn.execute('SELECT MAX(seq_id) FROM SeqTable').fetchone()

def writeMethodCall(transition):
    conn.execute('INSERT INTO SeqTable(time_stamp, touch_class, touch_mode) VALUES(?,?,?)', transition.getCursor())
    conn.commit()

def writeUserInfo(id, time):
    conn.execute('INSERT INTO UserTable(usr_id, time) VALUES(?,?)',(id, time))
    conn.commit()

def getLastUserId():
    return conn.execute('SELECT MAX(usr_id) FROM UserTable').fetchone()

