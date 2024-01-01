import src.m_lib.config.config as cn
from src.m_lib.utils.selects import GetValues

class VersionTables:

    def __init__(self, m_version_id) -> None:
        self.m_version_id = m_version_id
        self.tables = None

    def load_tables(self):
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

        cur = cn.con().cursor()
        conn = cn.con('new')
        cur_ins = conn.cursor()
        ins = 0
        for m_object_id, name in self.tables:
            cur.execute(''' SELECT lower(name) FROM sqlite_schema WHERE type ='table' and name = upper(?) ''', (name, ))

            r = cur.fetchone()
            (db_name, ) = r if r else None
            droped = 0 if db_name else 1

            cur_ins.execute(''' insert into m_object_detail (m_object_id, m_version_id, droped) values (?,?,?) ''', (m_object_id, self.m_version_id, droped))
            conn.commit()
            ins = ins +1

        cur.close()
        cur_ins.close()
        conn.close()

        print("Obj Details Table Ins", ins)


