import sqlite3

from src.db_autotest.m_lib.utils.connect_oracle import ConnectOracle
import configparser

def con(new = None):
    return Config.con(new)

def meta(new = None):
    return Config.meta(new)

# TODO add env creation in meta.m_env table

class Config:
    config  = configparser.ConfigParser()
    main_con = None
    main_env: str = None
    meta_con = None
    fetch_child_rows:int = 1000


    @classmethod
    def set_config(cls, config: configparser.ConfigParser):
        """
        docstring
        """
        cls.config = config
        cls.main_env = config.get('DEFAULT', 'main_env')
        cls.fetch_child_rows = config.getint('DEFAULT', 'fetch_child_rows')

    @classmethod
    def connect_main_sqlite(cls):
        db_main = cls.config[cls.main_env.upper()]
        return sqlite3.connect(db_main.get("db_path"))
        #print(cls.conn.total_changes)        

    @classmethod
    def con(cls, new = None):
        db_main = cls.config[cls.main_env.upper()]
        if cls.main_con is None:
            if db_main.get('db_type') == 'sqlite':
                cls.main_con = cls.connect_main_sqlite()
            else:
                cls.main_con = ConnectOracle.connect_main()

        if new is None:
            return cls.main_con
        else:
            if db_main.get('db_type') == 'sqlite':
                return cls.connect_main_sqlite()
            else:
                return ConnectOracle.connect_main()

    @classmethod
    def close_main(cls):
        if cls.main_con is not None:
            cls.main_con.close()


    @classmethod
    def meta(cls, new = None):
        if cls.meta_con is None:
            cls.meta_con = cls.connect_meta()

        if new is None:
            return cls.meta_con
        else:
            return cls.connect_meta()

    @classmethod
    def close_meta(cls):
        if cls.meta_con is not None:
            cls.meta_con.close

    @classmethod
    def connect_meta(cls):
        db_meta = cls.config['META_DB']
        return sqlite3.connect(db_meta.get('db_path'))
        #print(cls.meta_con.total_changes)         
