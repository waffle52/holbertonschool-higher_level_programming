#!/usr/bin/python3
""" prevents mysql injection """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    arg = sys.argv[4]
    cur.execute("""SELECT * FROM states WHERE BINARY name = %s ORDER BY
    states.id ASC;""", (arg,))
    result = cur.fetchall()

    for x in result:
        print(x)

    cur.close()
    db.close()
