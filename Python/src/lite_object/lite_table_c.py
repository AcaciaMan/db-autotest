from src.lib.m_object.m_class import M_Class
from src.lib.m_object.m_structure import M_Structure
from src.lite_object.lite_table_s import LiteTableS


class LiteTableC(M_Class):
    """
    docstring
    """
    def __init__(self, m_structure: M_Structure = LiteTableS()):
        super().__init__(m_structure)



