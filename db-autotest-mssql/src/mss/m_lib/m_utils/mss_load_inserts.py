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
select s.name, tab.name 
  from sys.tables tab, sys.objects o, sys.schemas s
  where 1=1
  and o.object_id = tab.object_id
  and o.schema_id = s.schema_id
  and tab.is_ms_shipped = 0
  and tab.type_desc = 'USER_TABLE'
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

    @staticmethod
    def insert_indexes():
        """
        docstring
        """

        cur = M_Config.con().cursor()

        cur.execute(
            """
select s.name, ix.name
  from sys.indexes ix, sys.tables tab, sys.objects o, sys.schemas s
  where 1= 1
  AND ix.object_id = tab.object_id
  and ix.object_id = o.object_id
  and o.schema_id = s.schema_id
  AND tab.is_ms_shipped = 0
  and tab.type_desc = 'USER_TABLE'
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
                (?, ?, 'INDEX')""",
                    x,
                )

            except Exception:
                existing = existing + 1

            else:
                # Commit your changes in the database
                M_Config.meta().commit()
                inserted = inserted + 1

        meta.close()

        print("Indexes Inserted:", inserted, "Existing", existing)

