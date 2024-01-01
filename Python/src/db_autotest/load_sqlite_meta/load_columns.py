import db_autotest.m_lib.m_config.config as cn

class LoadColumns(object):
    """
    docstring
    """
    def load(self):
        """
        docstring
        """

        cur = cn.con().cursor()

        cur.execute(
        '''
        WITH all_tables AS (SELECT name FROM sqlite_master WHERE type = 'table') 
        SELECT distinct 'db', lower(pti.name)
        FROM all_tables at INNER JOIN pragma_table_info(at.name) pti
        '''
        )

        lCur = cur.fetchall()

        cur.close

        #Connecting to sqlite
        meta = cn.meta().cursor()

        ins = 0
        exi = 0

        for x in lCur:
            # print("owner", owner, table_name)

            try:
                # Preparing SQL queries to INSERT a record into the database.
                meta.execute('''INSERT INTO M_OBJECT(
                SCHEMA, NAME, TYPE) VALUES 
                (?, ?, 'COLUMN')''', x)

            except Exception:
                exi = exi+1

            else:    

                # Commit your changes in the database
                cn.meta().commit()
                ins = ins+1

        meta.close()

        print("Columns ins", ins, "exi", exi)

