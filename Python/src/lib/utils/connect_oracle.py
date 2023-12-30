#import oracledb

class ConnectOracle(object):
    """
    docstring
    """

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