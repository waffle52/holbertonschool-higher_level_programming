#!/usr/bin/python3
""" prints from table where name is the same as input """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}'\
    ORDER BY states.id ASC;".format(sys.argv[4]))
    result = cur.fetchall()

    for x in result:
        print(x)
