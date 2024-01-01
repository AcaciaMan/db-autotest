import sqlite3

from src.db_autotest.m_lib.utils.connect_oracle import ConnectOracle

def con(new = None):
    return Config.con(new)

def meta(new = None):
    return Config.meta(new)

# TODO add env creation in meta.m_env table

class Config:
    prime_service = None
    conn = None
    db_host = None
    db_user = None
    db_pass = None
    db_type = None
    main_env = None
    meta_con = None
    env_dict = {}

    @classmethod
    def set_variables(cls, prime_service_):
        """
        docstring
        """
        cls.prime_service = prime_service_
        cls.main_env = cls.prime_service["main_env"]["name"]
        cls.retrieve_env(cls.prime_service["env"])
        cls.db_type = cls.env_dict[cls.main_env]["db_type"]

    @classmethod
    def retrieve_env(cls, thislist):
        for x in thislist:
            cls.env_dict.update(x)

    @classmethod
    def connect_main_sqlite(cls):
        return sqlite3.connect(cls.env_dict[cls.main_env]["db_path"])
        #print(cls.conn.total_changes)        

    @classmethod
    def con(cls, new = None):
        if cls.conn is None:
            if cls.db_type == 'sqlite':
                cls.conn = cls.connect_main_sqlite()
            else:
                ConnectOracle.connect_main()

        if new is None:
            return cls.conn
        else:
            return cls.connect_main_sqlite()

    @classmethod
    def close_main(cls):
        if cls.conn is not None:
            cls.conn.close


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
        return sqlite3.connect(cls.prime_service['metadata_db'])
        #print(cls.meta_con.total_changes)         
