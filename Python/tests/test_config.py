import unittest

from src.db_autotest.m_lib.config import config as cn  # noqa: E402

class Test_Config(unittest.TestCase):

    def test_access(self):
        print("Main env", cn.Config.main_env)


if __name__ == '__main__':
    unittest.main()