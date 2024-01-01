import unittest

from db_autotest.m_lib.m_config.config import M_Config

class Test_Config(unittest.TestCase):

    def test_access(self):
        print("Main env", M_Config.main_env)


if __name__ == '__main__':
    unittest.main()