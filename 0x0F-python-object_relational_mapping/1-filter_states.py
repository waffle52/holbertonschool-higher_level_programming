#!/usr/bin/python3
""" lists all states with a name starting with N """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    result = cur.fetchall()

    for x in result:
        if (x[1][0] == 'N'):
            print(x)
