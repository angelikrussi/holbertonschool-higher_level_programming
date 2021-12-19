#!/usr/bin/python3
'''
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * from states\
                WHERE name LIKE 'N%'\
                ORDER BY states.id")
    search = cursor.fetchall()
    for count in search:
        if count[1][0] == 'N':
            print(count)
    cursor.close()
    db.close()
