
import lib.config.config as cn


print('something main: ' + cn.Config.main_env)

print("Database version:", cn.con().total_changes)
