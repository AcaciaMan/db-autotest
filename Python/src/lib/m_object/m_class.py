from src.lib.m_object.m_structure import M_Structure
from src.lib.utils.m_entity_selects import get_entity_rows


class M_Class(object):
    """
    docstring
    """
    
    def __init__(self, m_structure: M_Structure):
        """
        docstring
        """
        self.m_structure = m_structure
        self.select: str = None
        self.where: str = None


    def load(self, m_id: list):
        """
        Load table
        Load parent structure
        """
        get_entity_rows(m_entity= self.m_structure.node, column=self.m_structure.node.id, value=m_id, fetch_rows=1, select=self.select, where=self.where)

        self.m_structure.load_nodes()