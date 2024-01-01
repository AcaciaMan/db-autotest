import db_autotest.m_lib.m_config.config as cn
from db_autotest.m_lib.m_utils.selects import GetValues

class VersionTabCols:

    def __init__(self, m_version_id) -> None:
        self.m_version_id = m_version_id
        self.tables = None

    def loadTabCols(self):
        """
        docstring
        """
        self.tables = GetValues.get_all_tables()
        self.load()


    def load(self):
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

        cur = cn.meta().cursor()
        conn = cn.meta('new')
        cur_ins = conn.cursor()
        ins = 0
        for m_object_id, name in self.tables:
            m_object_detail_id = GetValues.get_last_m_object_detail_id(m_object_id, cn.Config.main_env)

            cur.execute(''' select cid, lower(name), type from pragma_table_info(?) ''', (name, ))
            r = cur.fetchall()
            for col_cid, col_name, col_type in r:
                cur.execute(''' select m_object_id from m_object where type = 'COLUMN' and name=? ''', (col_name, ))
                r = cur.fetchone()
                m_column_object_id = r[0] if r else None



                cur_ins.execute(''' insert into m_column (m_object_detail_id, m_column_obj_id, sort, type) values (?,?,?,?) ''', (m_object_detail_id, m_column_object_id, col_cid, col_type))
                conn.commit()
                ins = ins +1

        cur.close()
        cur_ins.close()
        conn.close()

        print("Table Columns Ins", ins)


