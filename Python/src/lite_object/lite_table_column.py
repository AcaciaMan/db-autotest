from src.lib.m_object.m_entity import M_Entity
from src.lib.m_object.m_relation import M_Relation
from src.lib.m_table.m_table import m_column
from src.lite_object.lite_column import LiteColumn
from src.lite_object.lite_table import LiteTable


class LiteTableColumn(M_Relation):
    """
    docstring
    """
    def __init__(self, parent: M_Entity = LiteTable(), child: M_Entity = LiteColumn()):
        super().__init__(parent, child)


    def get_child_cols(self, ent: M_Entity):
        """
        docstring
        """
        return [m_column().m_object_detail_id]