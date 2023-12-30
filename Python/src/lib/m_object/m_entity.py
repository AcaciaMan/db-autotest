from src.lib.config.config import Config
from src.lib.m_object.m_str_type_enum import M_StructureType
from src.lib.m_table.m_row import M_Row
from src.lib.m_table.m_table import M_Table
from src.lib.utils.m_entity_utils import fill_entity_dict

class M_Entity(object):
    """
    docstring
    """
    def __init__(self, table: M_Table, row: M_Row, m_type: M_StructureType = M_StructureType.TOP, name: str = None):
        """
        docstring
        """
        self.row_cols = []
        self.row_data = ()
        self.row_dict = {}
        self.pretty_row = []    

        self.aliases = {}
        self.db_code = {}

        self.table = table
        self.row = row
        self.m_type = m_type

        self.id = []
        self.name = name

        self.rows = []
        self.i_row: int = None

    @property
    def row(self):
        """
        docstring
        """
        return self._row
    
    @row.setter
    def row(self, value: M_Row):
        """
        docstring
        """
        self._row = value
        self.pretty_row = self._row.c[Config.main_env]

    @property
    def name(self):
        """
        docstring
        """
        return self._name
    
    @name.setter
    def name(self, value: str):
        """
        docstring
        """
        self._name = value
        if value is None:
            self._name = type(self.table).__name__

    @property
    def rows(self):
        """
        docstring
        """
        return self._rows
    
    @rows.setter
    def rows(self, listvalue):
        """
        docstring
        """
        self._rows: list = listvalue
        if len(listvalue)>0:
            self._rows.sort(key=self.sortFunc)
            self.i_row = 0

    @property
    def i_row(self):
        """
        docstring
        """
        return self._i_row
    
    @i_row.setter
    def i_row(self, value):
        """
        docstring
        """
        self._i_row = value
        if self._i_row is not None:
            self.row_data = self.rows[self._i_row]
            fill_entity_dict(self)


    def __str__(self):
        """
        docstring
        """
        s = self.name + ': {'

        i = 0
        for x1 in self.pretty_row:

            if x1 in self.db_code:
                x3 = self.db_code[x1]
            else:
                x3 = x1

            x2 = [x3, self.row_dict[x1]]
            s = s + ': '.join(map(str, map(lambda x: f"'{x}'" if isinstance(x, str) else x, x2))) + ', '
            i=i+1
        
        if i>0:
            s= s[0:-2]

        s = s + '}'

        return s  
    
    def sortFunc(self, e):
        """
        docstring
        """
        return e[0]

    def copy_entity(self):
        """
        docstring
        """
        m_entity = M_Entity(self.table, self.row, self.m_type, self.name)

        m_entity.pretty_row = self.pretty_row   

        m_entity.aliases = self.aliases
        m_entity.db_code = self.db_code

        m_entity.id = self.id

        m_entity.sortFunc = self.sortFunc.__get__(m_entity)

        return m_entity
