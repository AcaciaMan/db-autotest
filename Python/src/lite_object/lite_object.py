from src.lib.m_object.m_entity import M_Entity
from src.lib.m_object.m_str_type_enum import M_StructureType
from src.lib.m_table.m_row import M_Row
from src.lib.m_table.m_row import m_object_r as rod
from src.lib.m_table.m_table import M_Table, m_object as tod

class LiteObject(M_Entity):
    def __init__(self, table: M_Table = tod(), row: M_Row = rod(), m_type: M_StructureType = M_StructureType.TOP):
        """
        docstring
        """
        super().__init__(table, row, m_type)
        self.id.append(tod().m_object_id)
        self.name = 'object'
