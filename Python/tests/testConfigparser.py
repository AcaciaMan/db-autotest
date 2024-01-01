import configparser

print(configparser.ConfigParser)

config = configparser.ConfigParser()

config['ENV'] = {'dev': {'db_type': 'sqlite',
      'db_path': 'C:/Work/GitHub/db-autotest/Docs/m_sqlite.db'}}

config['DEFAULT'] = {'main_env': 'dev'}

default = config['DEFAULT']

print(default.get('main_env'))