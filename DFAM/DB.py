import sqlite3, transition
DBFile = "BadUIDB"

class DBHelper(object):
    conn = sqlite3.connect(DBFile)

    def writeCOORD(x, y):
        conn.execute('INSERT INTO SeqTable(x,y) VALUES(?, ?)', (x,y))
        conn.commit()

    def writeMethodCall(transition):
        conn.execute('INSERT INTO SeqTable(timestamp, touch_class, touch_event) VALUES(?,?,?)', transition.getCursor())
