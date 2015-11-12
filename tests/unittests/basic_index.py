__author__ = 'bob.zhu'

import unittest
import sqlite3 as db

class app_setting_tests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_aa_sqlite_connection_test(self):
        print '.'*20+'test_aa_sqlite_connection_test'+'.'*20
        conn = db.connect("../../web/db.sqlite3")
        conn.row_factory = db.Row
        cursor = conn.cursor()
        cursor.execute('select * from auto_feature')
        rows = cursor.fetchall()
        for row in rows:
          print row['id']
        conn.close()
if __name__ == '__main__':
    unittest.main()