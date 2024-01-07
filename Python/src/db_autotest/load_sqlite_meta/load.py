from db_autotest.load_sqlite_meta.load_columns import LoadColumns
from db_autotest.load_sqlite_meta.load_indexes import LoadIndexes
from db_autotest.load_sqlite_meta.load_tables import LoadTables
from db_autotest.load_sqlite_meta.load_version import LoadVersion


class Load(object):
    """
    docstring
    """
    # TODO rewrite to use correct object names in correct capitalizing
    def load(self):
        """
        docstring
        """
        LoadTables().load()
        LoadIndexes().load()
        LoadColumns().load()
        LoadVersion().load()

     
        



