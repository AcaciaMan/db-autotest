import unittest
from src.load_sqlite_meta.load import Load  # noqa: F401

import src.load_sqlite_meta.load_tables as lt  # noqa: F401
from src.load_sqlite_meta.load_version import LoadVersion  # noqa: F401

class TestLoads(unittest.TestCase):

    def testTableLoad(self):
        print("Started")
        #lt.LoadTables().load()
        Load().load()
        #LoadVersion().load()
        
        


if __name__ == '__main__':
    unittest.main()