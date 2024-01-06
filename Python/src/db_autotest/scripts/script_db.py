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
                """, x)
        except Exception:
            print("Env already in meta db", x)

    M_Config.meta().commit()
    cur.close()
    return True
