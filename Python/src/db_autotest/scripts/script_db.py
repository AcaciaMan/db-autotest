from db_autotest.load_mssql_meta.mss_load_inserts import MSS_LoadInserts
from db_autotest.load_mssql_meta.mss_load_version_indexes import MSS_LoadVersionIndexes
from db_autotest.load_mssql_meta.mss_load_version_tables import MSS_LoadVersionTables
from db_autotest.load_sqlite_meta.load import Load
from db_autotest.m_lib.m_config.config import M_Config


def script_add_ini_envs_to_meta_db():
    """
    # read config envs
    # insert into meta m_env table
    """
    cur = M_Config.meta().cursor()
    for x in M_Config.env_dict.keys():
        try:
            cur.execute("""
                insert into m_env (name) values (?)
                """, (x,))
        except Exception as e:  # noqa: F841
            # print(e)
            print("Env already in meta db", x)

    M_Config.meta().commit()
    cur.close()
    return True


def script_load_db_meta_structure():
    """
    docstring
    """
    db_main = M_Config.config[M_Config.main_env.upper()]
    db_type = db_main.get('db_type')
    if db_type == 'mssql':
        MSS_LoadInserts.insert_tables()
        MSS_LoadInserts.insert_indexes()
        MSS_LoadInserts.insert_columns()
        inserted_id = MSS_LoadInserts.insert_version()
        v_tables = MSS_LoadVersionTables(inserted_id)
        v_tables().insert_into_meta_db()
        v_tables.insert_columns()
        v_indexes = MSS_LoadVersionIndexes(inserted_id)
        v_indexes().insert_into_meta_db()
        v_indexes.insert_columns()

    elif db_type == 'sqlite':
        Load().load()

