import yaml
from . import config as cn
import os

prime_service = None

with open('config.yaml', 'r') as file:
   print(os.path.abspath(  'config.yaml'))
   prime_service = yaml.safe_load(file)


print(dir(cn))
cn.Config.set_variables(prime_service)

#cn.connect_main()