import db_autotest.m_lib.m_config.config as cn

class LoadTables(object):
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
        SELECT 
            'db', lower(name)
        FROM 
            sqlite_schema
        WHERE 
            type ='table'
        '''
        )

        lCur = cur.fetchall()

        cur.close

        #Connecting to sqlite
        meta = cn.meta().cursor()

        inserted = 0
        existing = 0

        for x in lCur:
            # print("owner", owner, table_name)

            try:
                # Preparing SQL queries to INSERT a record into the database.
                meta.execute('''INSERT INTO M_OBJECT(
                SCHEMA, NAME, TYPE) VALUES 
                (?, ?, 'TABLE')''', x)

            except Exception:
                existing = existing + 1

            else:    

                # Commit your changes in the database
                cn.meta().commit()
                inserted = inserted + 1

        meta.close()

        print("Tables Inserted:", inserted, "Existing", existing)

