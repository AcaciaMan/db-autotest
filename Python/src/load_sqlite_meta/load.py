import src.lib.config.config as cn  # noqa: F401

from src.load_sqlite_meta.load_columns import LoadColumns
from src.load_sqlite_meta.load_indexes import LoadIndexes
from src.load_sqlite_meta.load_tables import LoadTables
from src.load_sqlite_meta.load_version import LoadVersion


class Load(object):
    """
    docstring
    """
    
    def load(self):
        """
        docstring
        """
        LoadTables().load()
        LoadIndexes().load()
        LoadColumns().load()
        LoadVersion().load()

     
        



