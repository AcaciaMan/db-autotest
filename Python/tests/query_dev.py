
import db_autotest.m_lib.m_config.config as cn


print('something main: ' + cn.Config.main_env)

print("Database version:", cn.con().total_changes)
