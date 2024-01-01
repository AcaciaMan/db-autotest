import unittest

from src.db_autotest.m_lib.utils.generate_tab_cols import GenerateTabCols

class TestGen(unittest.TestCase):

    def testGen(self):
        print("Started Gen")
        GenerateTabCols.delete_prev_tables()
        GenerateTabCols.insert_tables()

        GenerateTabCols.delete_prev_rows()
        GenerateTabCols.insert_rows()        
        

if __name__ == '__main__':
    unittest.main()