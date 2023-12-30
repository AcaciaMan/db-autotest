from src.lib.m_object.m_entity import M_Entity
from src.lib.m_object.m_str_type_enum import M_StructureType
from src.lib.m_object.m_structure import M_Structure
from src.lite_object.lite_object import LiteObject

class LiteObjectS(M_Structure):
    """
    docstring
    """
    def __init__(self, m_entity: M_Entity = LiteObject(), m_type: M_StructureType = M_StructureType.PARENT):
        super().__init__(m_entity, m_type)
