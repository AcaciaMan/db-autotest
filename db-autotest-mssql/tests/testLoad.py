import unittest

from db_autotest.scripts.script_db import script_load_db_meta_structure

class TestLoads(unittest.TestCase):

    def testTableLoad(self):
        print("Started")
        #lt.LoadTables().load()
        script_load_db_meta_structure()
        #LoadVersion().load()
        

if __name__ == '__main__':
    unittest.main()