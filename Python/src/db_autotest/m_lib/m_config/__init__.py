import configparser
from . import config as cn
import os

file_path = os.environ.get('DB_AUTOTEST_CONFIG_FILE', 'db_autotest.ini')
config_default = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

try:
    lstPaths = config_default.read(file_path)
    db_main = config_default[config_default.get('DEFAULT', 'main_env').upper()]
    print(config_default.get('DEFAULT', 'main_env'))    
    db_main = config_default[config_default.get('DEFAULT', 'main_env').upper()]
    print('DB_TYPE', db_main.get('db_type'))
    cn.M_Config.set_config(config_default)

except Exception as e:
   print('Error', e)


#cn.connect_main()