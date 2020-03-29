#!/usr/bin/python3
""" prints from table where name is the same as input """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    com = ("""SELECT * FROM states WHERE BINARY name='{}'
    ORDER BY states.id ASC;""".format(sys.argv[4]))
    cur.execute(com)
    result = cur.fetchall()

    for x in result:
        print(x)

    cur.close()
    db.close()
