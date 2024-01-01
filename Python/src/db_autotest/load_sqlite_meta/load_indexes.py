import db_autotest.m_lib.m_config.config as cn

class LoadIndexes(object):
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
            type ='index'
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
                (?, ?, 'INDEX')''', x)

            except Exception:
                exi = exi +1

            else:    

                # Commit your changes in the database
                cn.meta().commit()
                ins = ins +1

        meta.close()

        print("Indexes Inserted", ins, "Existing", exi)

