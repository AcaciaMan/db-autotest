import sqlite3
import configparser
from db_autotest.m_lib.m_utils.connect_db import M_ConnectFactory, M_Connect

class M_Config:
    config: configparser.ConfigParser = None
    main_con = None
    meta_con = None
    main_env: str = None
    fetch_child_rows:int = 1000
    env_dict = {}


    @classmethod
    def set_config(cls, config: configparser.ConfigParser):
        """
        docstring
        """
        cls.close_main()
        cls.close_meta()
        cls.config = config
        cls.main_env = config.get('DEFAULT', 'main_env')
        cls.fetch_child_rows = config.getint('DEFAULT', 'fetch_child_rows')
        cls.env_dict = {}
        for x in cls.config.get('DEFAULT','envs').split(','):
            cls.env_dict[x] = x.upper()

 

    @classmethod
    def con(cls, new = None):
        db_main = cls.config[cls.main_env.upper()]
        if cls.main_con is None:
            cls.main_con = M_ConnectFactory().create_connect(db_main.get('db_type')).getConn()

        if new is None:
            return cls.main_con
        else:
            return M_ConnectFactory().create_connect(db_main.get('db_type')).getConn()

    @classmethod
    def close_main(cls):
        if cls.main_con is not None:
            cls.main_con.close()
            cls.main_con = None


    @classmethod
    def meta(cls, new = None) -> sqlite3.Connection:
        if cls.meta_con is None:
            cls.meta_con = M_Connect.getMeta()

        if new is None:
            return cls.meta_con
        else:
            return M_Connect.getMeta()

    @classmethod
    def close_meta(cls):
        if cls.meta_con is not None:
            cls.meta_con.close
            cls.meta_con = None

