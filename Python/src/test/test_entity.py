import unittest
from src.lib.utils.m_yaml import M_Yaml
from src.lite_object.c_m_table import C_M_Table
from src.lite_object.c_m_table_names import C_M_TableNames
from src.lite_object.lite_table_c import LiteTableC

class TestLoads(unittest.TestCase):

    def testLoadClass(self):
        print('Started class')
        cl = LiteTableC()
        cl.load([4])
        print(M_Yaml().get_yaml(cl.m_structure))

    def testLoadInit(self):
        print('Started init')
        cl = C_M_Table()
        cl.c_main.load([4])
        print(M_Yaml().get_yaml(cl.c_main.m_structure))

    def testLoadNames(self):
        print('Started names')
        cl = C_M_TableNames()
        cl.c_main.load([4])
        print(M_Yaml().get_yaml(cl.c_main.m_structure))



if __name__ == '__main__':
    unittest.main()