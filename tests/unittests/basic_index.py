__author__ = 'bob.zhu'

import unittest
import sqlite3

class app_setting_tests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_aa_sqlite_connection_test(self):
        print '.'*20+'test_aa_sqlite_connection_test'+'.'*20
        cx = sqlite3.connect("../../web/db.sqlite3")

if __name__ == '__main__':
    unittest.main()