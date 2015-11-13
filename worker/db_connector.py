__author__ = 'bob.zhu'
import sqlite3 as db

class sqlite_db_connector:
    @staticmethod
    def get_connection():
        conn = db.connect("../../web/db.sqlite3")
        conn.row_factory = db.Row
        cursor = conn.cursor()
        return conn, cursor
