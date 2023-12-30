import src.lib.config.config as cn
from src.lib.utils.selects import GetValues

class VersionIndexes:

    def __init__(self, m_version_id) -> None:
        self.m_version_id = m_version_id
        self.indexes = None

    def load_indexes(self):
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
        INSERT INTO M_OBJECT_DETAIL (
                                        M_OBJECT_DETAIL_ID,
                                        M_OBJECT_ID,
                                        M_VERSION_ID,
                                        IDX_TABLE_ID,
                                        [UNIQUE],
                                        DROPED
        '''

        cur = cn.con().cursor()
        conn = cn.con('new')
        cur_ins = conn.cursor()
        ins = 0
        for m_object_id, name in self.indexes:
            cur.execute(''' SELECT lower(name), lower(tbl_name) FROM sqlite_schema WHERE type ='index' and upper(name) = upper(?) ''', (name, ))

            r = cur.fetchone()
            db_name = r[0] if r else None
            tbl_name = r[1] if r else None
            droped = 0 if db_name else 1

            cur.execute(''' SELECT m_object_id FROM m_object WHERE type ='TABLE' and name = ? ''', (tbl_name, ))
            r = cur.fetchone()
            tbl_id = r[0] if r else None

            cur.execute(''' select [unique] from PRAGMA_INDEX_LIST(?) where upper(name) = upper(?) ''', (tbl_name, name))
            r = cur.fetchone()
            is_unique = r[0] if r else 0

            cur_ins.execute(''' insert into m_object_detail (m_object_id, m_version_id, idx_table_id, m_unique, droped) values (?,?,?,?,?) ''', (m_object_id, self.m_version_id, tbl_id, is_unique, droped))
            conn.commit()
            ins = ins +1

        cur.close()
        cur_ins.close()
        conn.close()

        print("Obj Details Index Ins", ins)


