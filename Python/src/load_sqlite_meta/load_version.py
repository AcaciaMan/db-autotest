# Create version
# Load version tables
# Load version indexes
# Load version tables columns
# Load version indexes columns


# Select version id
from src.lib.utils.selects import GetValues
from src.load_sqlite_meta.load_version_idx_cols import VersionIdxCols
from src.load_sqlite_meta.load_version_indexes import VersionIndexes
from src.load_sqlite_meta.load_version_tab_cols import VersionTabCols
import src.load_sqlite_meta.load_version_tables as vt
import src.lib.config.config as cn


class LoadVersion(object):
    """
    docstring
    """
    def load(self):
        """
        docstring
        """

        m_env_id = GetValues.get_m_env_id()

        cur = cn.meta().cursor()


        cur.execute(
        '''
        insert into m_version (m_env_id) values (?) returning m_version_id
        ''', (m_env_id,)
        )

        r = cur.fetchone()
        (inserted_id, ) = r if r else None
        print('ins_id', inserted_id)

        cur.close()
        cn.meta().commit()

        iVT = vt.VersionTables(inserted_id)
        iVT.load_tables()

        VersionIndexes(inserted_id).load_indexes()

        VersionTabCols(inserted_id).loadTabCols()
        VersionIdxCols(inserted_id).loadIdxCols()
