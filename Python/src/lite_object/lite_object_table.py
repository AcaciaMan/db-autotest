from src.lib.m_object.m_entity import M_Entity
from src.lib.m_object.m_relation import M_Relation
from src.lite_object.lite_object import LiteObject
from src.lite_object.lite_table import LiteTable


class LiteObjectTable(M_Relation):
    """
    docstring
    """
    def __init__(self, parent: M_Entity = LiteObject(), child: M_Entity = LiteTable()):
        super().__init__(parent, child)

