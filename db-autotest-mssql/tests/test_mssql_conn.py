import unittest
import pyodbc


from db_autotest.m_lib.m_config.config import M_Config

class Test_Config(unittest.TestCase):

    def test_access(self):
        print("Main env", M_Config.main_env)

    def test_select_alltables(self):
        """
        docstring
        """
        db_mssql = M_Config.config[M_Config.main_env.upper()]
        conn = pyodbc.connect(db_mssql.get('conn_str')) 


        SQL_QUERY = """
        select table_schema, table_name 
        from information_schema.tables
        where 1=1
        and TABLE_TYPE = 'BASE TABLE'    
        """

        cursor = conn.cursor()
        cursor.execute(SQL_QUERY)

        records = cursor.fetchall()
        for i, r in enumerate(records):
            print(f"{r.table_schema}\t{r.table_name}")
            if i == 10:
                break


if __name__ == '__main__':
    unittest.main()