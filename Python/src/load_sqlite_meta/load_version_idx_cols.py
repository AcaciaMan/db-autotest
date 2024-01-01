import src.m_lib.config.config as cn
from src.m_lib.utils.selects import GetValues

class VersionIdxCols:

    def __init__(self, m_version_id) -> None:
        self.m_version_id = m_version_id
        self.indexes = None
        self.m_env_id = GetValues.get_m_env_id()

    def loadIdxCols(self):
        """
        docstring
        """
        self.indexes = GetValues.get_all_indexes()
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
        for m_object_id, name in self.indexes:
            cur.execute(''' SELECT o.m_object_detail_id
                        FROM m_object_detail o, m_version v
                        WHERE o.m_object_id = ? 
                        and o.m_version_id = v.m_version_id
                        and v.m_env_id = ?
                        order by v.load_date desc ''', (m_object_id, self.m_env_id))
            r = cur.fetchone()
            m_object_detail_id = r[0] if r else None

            cur.execute(''' select seqno, lower(name) from pragma_index_info(?) ''', (name, ))
            r = cur.fetchall()
            for col_seqno, col_name in r:
                cur.execute(''' select m_object_id from m_object where type = 'COLUMN' and name=? ''', (col_name, ))
                r = cur.fetchone()
                m_column_object_id = r[0] if r else None



                cur_ins.execute(''' insert into m_column (m_object_detail_id, m_column_obj_id, sort) values (?,?,?) ''', (m_object_detail_id, m_column_object_id, col_seqno))
                conn.commit()
                ins = ins +1

        cur.close()
        cur_ins.close()
        conn.close()

        print("Index Columns Ins", ins)


