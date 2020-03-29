#!/usr/bin/python3
""" lists all cities by given database """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM cities ORDER BY
    cities.id ASC;""")
    result = cur.fetchall()

    for x in result:
        print(x)

    cur.close()
    db.close()
