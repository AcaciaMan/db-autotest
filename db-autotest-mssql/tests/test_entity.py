import unittest
from db_autotest.m_lib.m_utils.m_yaml import M_Yaml
from mss.m_company_object.c_m_person import C_M_Person

class TestLoads(unittest.TestCase):

    def testLoadInit(self):
        print('Started init')
        cl = C_M_Person()
        cl.c_main.load([2])
        print(M_Yaml().get_yaml(cl.c_main.m_structure))


if __name__ == '__main__':
    unittest.main()