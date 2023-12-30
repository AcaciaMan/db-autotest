from src.lib.m_object.m_entity import M_Entity
from src.lib.m_object.m_str_type_enum import M_StructureType
from src.lib.m_object.m_structure import M_Structure
from src.lite_object.lite_column_s import LiteColumnS
from src.lite_object.lite_object_s import LiteObjectS
from src.lite_object.lite_object_table import LiteObjectTable
from src.lite_object.lite_table import LiteTable
from src.lite_object.lite_table_column import LiteTableColumn


class LiteTableS(M_Structure):
    """
    docstring
    """
    def __init__(self, m_entity: M_Entity = LiteTable(), m_type: M_StructureType = M_StructureType.TOP):
        super().__init__(m_entity, m_type)
        self.parent.append([LiteObjectS(), LiteObjectTable()])
        self.child.append([LiteColumnS(), LiteTableColumn()])