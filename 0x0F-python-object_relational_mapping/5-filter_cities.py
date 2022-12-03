#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys
from sys import argv


def connection(username, passwd, database):
    """..."""
    try:
        return MySQLdb.connect(host='localhost',
                               port=3306,
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3])

    except Exception:
        print("cant connect to database")


if __name__ == '__main__':
    db = connection(argv[1], argv[2], argv[3])
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    try:
        cur.execute("""SELECT c.name
                    FROM cities AS c
                    INNER JOIN states AS s
                    ON c.state_id = s.id
                    WHERE s.name = '{}'
                    ORDER BY state_id ASC""".format(sys.argv[4]))
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s".format(e.sys.argv[0], e.sys.argv[1]))
        except IndexError:
            print("MySQL Error: %s".format(str(e)))

    print(*[row[0] for row in rows], sep=', ')
    cur.close()
    db.close()
