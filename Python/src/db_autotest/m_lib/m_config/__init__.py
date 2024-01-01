import configparser
from . import config as cn
import os

file_path = os.environ.get('DB_AUTOTEST_CONFIG_FILE', 'db_autotest.ini')
config_default = configparser.ConfigParser()

try:
    config_default.read(file_path)
    print(config_default.get('DEFAULT', 'main_env'))    
    cn.M_Config.set_config(config_default)

except Exception as e:
   print('Error', e)


#cn.connect_main()