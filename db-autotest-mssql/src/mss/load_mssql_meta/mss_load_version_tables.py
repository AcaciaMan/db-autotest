from typing import Any
from db_autotest.m_lib.m_utils.selects import GetValues
from db_autotest.m_lib.m_config.config import M_Config

class MSS_LoadVersionTables(object):
    """
    docstring
    """
    def __init__(self, m_version_id):
        """
        docstring
        """
        self.m_version_id = m_version_id
        self.tables = []
        self.l_tables = []

    def __call__(self, *args: Any, **kwds: Any):
        self.tables = list(GetValues.get_all_tables())
        return self
    

    def insert_into_meta_db(self):
        """
        docstring
        """
        '''
        INSERT INTO M_OBJECT_DETAIL (
                                        M_OBJECT_DETAIL_ID,
                                        M_OBJECT_ID,
                                        M_VERSION_ID,
                                        DROPED
                                    )
                                    VALUES (
                                        'M_OBJECT_DETAIL_ID',
                                        'M_OBJECT_ID',
                                        'M_VERSION_ID',
                                        'DROPED'
                                    );
        '''

        cur = M_Config.con().cursor()
        cur_ins = M_Config.meta().cursor()
        ins = 0
        for r_t in self.tables:
            l_t = list(r_t)
            [m_object_id, schema, name] = l_t
            cur.execute(''' 
                select tab.object_id 
                from sys.tables tab, sys.objects o, sys.schemas s
                where 1=1
                and o.object_id = tab.object_id
                and o.schema_id = s.schema_id
                and tab.is_ms_shipped = 0
                and tab.type_desc = 'USER_TABLE' 
                and s.name = ?
                and tab.name = ?
                ''', (schema, name))

            r = cur.fetchone()
            mssql_id = r[0] if r else None
            droped = 0 if mssql_id else 1

            cur_ins.execute(''' insert into m_object_detail (m_object_id, m_version_id, droped) values (?,?,?) ''', (m_object_id, self.m_version_id, droped))
            inserted_id = cur_ins.lastrowid

            l_t.append(droped)
            l_t.append(inserted_id)
            l_t.append(mssql_id)

            self.l_tables.append(l_t)

            M_Config.meta().commit()
            ins = ins +1

        cur.close()
        cur_ins.close()

        print("Obj Details Table Ins", ins)        


    def insert_columns(self):
        """
        docstring
        """
        '''
        INSERT INTO M_COLUMN (
                                        M_COLUMN_ID,
                                        M_OBJECT_DETAIL_ID,
                                        M_COLUMN_OBJ_ID,
                                        SORT,
                                        TYPE
                                    )
        '''

        cur = M_Config.con().cursor()
        cur_ins = M_Config.meta().cursor()
        ins = 0
        for l_t in self.l_tables:
            [m_object_id, schema, name, droped, m_object_detail_id, mssql_id] = l_t
            
            if droped == 1:
                continue
            cur.execute(
                """ 
                select  col.column_id,
    col.name as column_name, 
    t.name as data_type    
from sys.tables as tab
    inner join sys.columns as col
        on tab.object_id = col.object_id
    left join sys.types as t
    on col.user_type_id = t.user_type_id
where 1=1
  and t.name not in ('binary', 'varbinary', 'image') 
  and tab.object_id = ?
                """,
                (mssql_id,)
            )
            r = cur.fetchall()
            for col_cid, col_name, col_type in r:
                cur_ins.execute(
                    """ select m_object_id from m_object where type = 'COLUMN' and schema = ? and name=? """,
                    (schema, col_name)
                )
                r = cur_ins.fetchone()
                m_column_object_id = r[0] if r else None

                cur.execute(
                """
                SELECT 1
FROM sys.indexes AS i
INNER JOIN sys.index_columns AS ic ON i.OBJECT_ID = ic.OBJECT_ID
       AND i.index_id = ic.index_id
WHERE i.is_primary_key = 1
and ic.object_id = ?
and ic.column_id = ?
                """, (mssql_id, col_cid))
                r = cur.fetchone()
                pk = r[0] if r else 0

                cur_ins.execute(
                    """ insert into m_column (m_object_detail_id, m_column_obj_id, sort, type, pk) values (?,?,?,?,?) """,
                    (m_object_detail_id, m_column_object_id, col_cid, col_type, pk)
                )

                M_Config.meta().commit()
                ins = ins +1

        cur.close()
        cur_ins.close()

        print("M_Column Table Ins", ins)      