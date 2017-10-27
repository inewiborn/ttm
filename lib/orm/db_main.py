import os
import sys
import sqlite3

class DBMain:
    def __init__(self):
        self.con = sqlite3.connect(sys.path[0] + '/ttm.db')
        self.cur = con.cursor()
        con.close()
    def query(self, sql):
        try:
            self.cur.executescript(sql)
        except sqlite3.DatabaseError as err:
            print('Error', err)
        else
            print('Query sucesfull')

    def initDb(self):
        sql = """\
        CREATE TABLE project(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            dir TEXT
        );
        """
        self.query(sql)
        sql = """\
        CREATE TABLE task(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_project INTEGER,
            description TEXT
        )
        """
        self.query(sql)
