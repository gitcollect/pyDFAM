import sqlite3, transition
DBFile = "BadUIDB"

class DBHelper(object):
    conn = sqlite3.connect(DBFile)

    def writeCOORD(timestamp, x, y):
    
        def getTimestampSeq():
            return conn.execute('SELECT seq_id, time_stamp from SeqTable;').fetchall()
        
        seqs = getTimestampSeq()

        filter(lambda x : x[0] < )

        conn.execute('INSERT INTO COORDTable(x,y) VALUES(?, ?)', (x,y))
        conn.commit()

    def writeMethodCall(transition):
        conn.execute('INSERT INTO SeqTable(timestamp, touch_class, touch_event) VALUES(?,?,?)', transition.getCursor())
