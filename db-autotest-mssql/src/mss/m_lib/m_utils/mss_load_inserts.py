from db_autotest.m_lib.m_config.config import M_Config


class MSS_LoadInserts(object):
    """
    docstring
    """

    @staticmethod
    def insert_tables():
        """
        docstring
        """

        cur = M_Config.con().cursor()

        cur.execute(
            """
select table_schema, table_name 
  from information_schema.tables
  where 1=1
  and TABLE_TYPE = 'BASE TABLE' 
        """
        )

        lCur = cur.fetchall()

        cur.close()

        # Connecting to sqlite
        meta = M_Config.meta().cursor()

        inserted = 0
        existing = 0

        for x in lCur:
            # print("owner", owner, table_name)

            try:
                # Preparing SQL queries to INSERT a record into the database.
                meta.execute(
                    """INSERT INTO M_OBJECT(
                SCHEMA, NAME, TYPE) VALUES 
                (?, ?, 'TABLE')""",
                    x,
                )

            except Exception:
                existing = existing + 1

            else:
                # Commit your changes in the database
                M_Config.meta().commit()
                inserted = inserted + 1

        meta.close()

        print("Tables Inserted:", inserted, "Existing", existing)
