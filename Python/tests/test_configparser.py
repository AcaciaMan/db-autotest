import unittest
import configparser
import os

from src.db_autotest.m_lib.m_config.config import M_Config

class TestLoads(unittest.TestCase):
  
    def testConfig(self):
        """
        docstring
        """

        print(configparser.ConfigParser)

        config = configparser.ConfigParser()

        config['ENV'] = {'dev': 
            {'db_type': 'sqlite',
            'db_path': 'C:/Work/GitHub/db-autotest/Docs/m_sqlite.db'}
            }

        config['META_DB'] = {'db_path': 'C:/Work/GitHub/db-autotest/Docs/m_sqlite.db'}

        config['DEFAULT'] = {'main_env': 'dev', 'fetch_child_rows': 1000}

        default = config['DEFAULT']

        print(default.get('main_env'))

        #with open('example.ini', 'w') as configfile:
        #    config.write(configfile)


    def get_config_file(self):
        env = os.environ.get('DB_AUTOTEST_CONFIG_FILE', 'db_autotest.toml')
        return env

    def testLaodDefaultConfig(self):
        """
        docstring
        """
        CONFIG_FILE = self.get_config_file()
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        print(config.get('DEFAULT', 'main_env'))

    def testLoadCn(self):
        """
        docstring
        """
        print(M_Config.config.get('DEFAULT','main_env'))


if __name__ == '__main__':
      unittest.main()


