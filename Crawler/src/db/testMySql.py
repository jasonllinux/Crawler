__author__ = 'Jason'

import MySQLdb as mdb
import MySQLdb.cursors

def test_db():
    pass
    con = None
    try:
        con = mdb.connect('localhost', 'root', '363363', 'test')

        cur = con.cursor()
        cur.execute("select version()")
        data = cur.fetchone()
        print "DataBase version: %s " % data
        pass

    finally:
        if con:
            con.close()


if __name__ == '__main__':
    print 'test'
    test_db()
