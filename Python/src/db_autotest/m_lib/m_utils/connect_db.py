#import oracledb
import importlib
import sqlite3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db_autotest.m_lib.m_config import config

class M_Connect(object):
    """
    docstring
    """

    def __init__(self, type = 'sqlite'):
        self.config: config = importlib.import_module('db_autotest.m_lib.m_config.config')
        self.type = type


    def getConn(self):
        db_main = self.config.M_Config.config[self.config.M_Config.main_env.upper()]
        conn = sqlite3.connect(db_main.get("db_path"))
        return conn
    
    def getMeta(self):
        db_meta = self.config.M_Config.config['META_DB']
        conn = sqlite3.connect(db_meta.get('db_path'))
        return conn


class M_ConnectMssql(M_Connect):
    """
    docstring
    """
    def __init__(self, type = 'mssql'):
        """
        docstring
        """
        super().__init__(type)

    def getConn(self):
        m_pyodbc = importlib.import_module('pyodbc')
        db_main = self.config.M_Config.config[self.config.M_Config.main_env.upper()]
        conn = m_pyodbc.connect(db_main.get('conn_str')) 
        return conn


""""
    @classmethod
    def connect_main(cls):
        oracledb = __import__('oracledb')
        params = oracledb.ConnectParams(
            host=cls.env_dict[cls.main_env]["db_host"],
            port=cls.env_dict[cls.main_env]["db_port"],
            service_name=cls.env_dict[cls.main_env]["db_service_name"],
        )
        cls.conn = oracledb.connect(
            user=cls.env_dict[cls.main_env]["db_user"],
            password=cls.env_dict[cls.main_env]["db_pass"],
            params=params,
        )
        print(cls.conn.version)
"""

class M_ConnectFactory:
    def create_connect(self, type):
        if type == 'sqlite':
            return M_Connect()
        elif type == 'mssql':
            return M_ConnectMssql()
        