from typing import Any
from db_autotest.m_lib.m_utils.selects import GetValues
from db_autotest.m_lib.m_config.config import M_Config


class MSS_LoadVersionIndexes(object):
    """
    docstring
    """

    def __init__(self, m_version_id):
        """
        docstring
        """
        self.m_version_id = m_version_id
        self.indexes = []
        self.l_indexes = []

    def __call__(self, *args: Any, **kwds: Any):
        self.indexes = GetValues.get_all_indexes()
        return self

    def insert_into_meta_db(self):
        """
        docstring
        """
        """
        INSERT INTO M_OBJECT_DETAIL (
                                        M_OBJECT_DETAIL_ID,
                                        M_OBJECT_ID,
                                        M_VERSION_ID,
                                        IDX_TABLE_ID,
                                        M_UNIQUE,
                                        STATUS,
                                        ENABLED,
                                        DROPED
                                    )
        """

        cur = M_Config.con().cursor()
        cur_ins = M_Config.meta().cursor()
        ins = 0
        for r_t in self.indexes:
            l_t = list(r_t)
            [m_object_id, schema, name] = l_t
            cur.execute(
                """ 
select i.object_id, i.index_id, i.is_unique, i.is_disabled, OBJECT_NAME(i.OBJECT_ID) AS TableName from sys.indexes i, sys.tables tab 
  where 1=1
  and i.object_id = tab.object_id
  and schema_name(tab.schema_id) = ?
  and i.name = ?
                """,
                (schema, name),
            )

            r = cur.fetchone()
            mssql_id = r[0] if r else None
            index_id = r[1] if r else None
            m_unique = r[2] if r else None
            disabled = r[3] if r else 1
            enabled = 1 if disabled == 0 else 0
            tbl_name = r[4] if r else None
            droped = 0 if mssql_id else 1

            cur_ins.execute(
                """ SELECT m_object_id FROM m_object WHERE type ='TABLE' and schema = ? and name = ? """,
                (schema, tbl_name)
            )
            r = cur_ins.fetchone()
            tbl_id = r[0] if r else None

            cur_ins.execute(
                """ insert into m_object_detail (m_object_id, m_version_id, idx_table_id, m_unique, enabled, droped) values (?,?,?,?,?,?) """,
                (m_object_id, self.m_version_id, tbl_id, m_unique, enabled, droped)
            )
            inserted_id = cur_ins.lastrowid

            l_t.append(droped)
            l_t.append(inserted_id)
            l_t.append(mssql_id)
            l_t.append(index_id)

            self.l_indexes.append(l_t)

            M_Config.meta().commit()
            ins = ins + 1

        cur.close()
        cur_ins.close()

        print("Obj Details Indexes Ins", ins)

    def insert_columns(self):
        """
        docstring
        """
        """
        INSERT INTO M_COLUMN (
                                        M_COLUMN_ID,
                                        M_OBJECT_DETAIL_ID,
                                        M_COLUMN_OBJ_ID,
                                        SORT
                                    )
        """

        cur = M_Config.con().cursor()
        cur_ins = M_Config.meta().cursor()
        skiped = 0
        ins = 0
        for l_t in self.l_indexes:
            [m_object_id, schema, name, droped, m_object_detail_id, mssql_id, index_id] = l_t

            if droped == 1:
                continue
            cur.execute(
                """ 
select ic.index_column_id, COL_NAME(ic.OBJECT_ID,ic.column_id) AS ColumnName
  from sys.index_columns AS ic
  where ic.object_id = ?
  and ic.index_id = ?
                """,
                (mssql_id,index_id)
            )
            r = cur.fetchall()
            for col_cid, col_name in r:
                cur_ins.execute(
                    """ select m_object_id from m_object where type = 'COLUMN' and schema = ? and name=? """,
                    (schema, col_name),
                )
                r = cur_ins.fetchone()
                m_column_object_id = r[0] if r else None

                if m_column_object_id:
                    
                    cur_ins.execute(
                        """ insert into m_column (m_object_detail_id, m_column_obj_id, sort) values (?,?,?) """,
                        (m_object_detail_id, m_column_object_id, col_cid)
                    )

                    M_Config.meta().commit()
                    ins = ins + 1
                else:
                    skiped = skiped + 1

        cur.close()
        cur_ins.close()

        print("M_Column Table Index Ins", ins, "skiped", skiped)
