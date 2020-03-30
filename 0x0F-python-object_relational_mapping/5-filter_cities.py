#!/usr/bin/python3
""" """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name, states.name
    FROM cities JOIN states ON states.id = cities.state_id
    WHERE states.name like '{}' ORDER BY cities.id ASC""".format(sys.argv[4]))
    result = cur.fetchall()

    print(", ".join(row[0] for row in result))

    cur.close()
    db.close()
