import unittest
from db_autotest.lite_object.c_m_table import C_M_Table
from db_autotest.m_lib.m_utils.m_yaml import M_Yaml
from db_autotest.lite_object.c_m_table_names import C_M_TableNames

class TestLoads(unittest.TestCase):

    def testLoadInit(self):
        print('Started init')
        cl = C_M_Table()
        cl([4])
        print(M_Yaml().get_yaml(cl.main_class.m_structure))

    def testLoadNames(self):
        print('Started names')
        cl = C_M_TableNames()
        cl([4])
        print(M_Yaml().get_yaml(cl.main_class.m_structure))



if __name__ == '__main__':
    unittest.main()