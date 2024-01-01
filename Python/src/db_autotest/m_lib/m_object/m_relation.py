from src.db_autotest.m_lib.m_config.config import M_Config
from src.db_autotest.m_lib.m_object.m_entity import M_Entity
from src.db_autotest.m_lib.m_object.m_structure import M_Structure
from src.db_autotest.m_lib.m_utils.m_entity_selects import get_entity_rows


class M_Relation(object):
    """
    docstring
    """

    relations = {}

    def __init__(self, parent: M_Entity, child: M_Entity, fetch_rows: int = M_Config.fetch_child_rows):
        """
        docstring
        """
        self.parent = parent
        self.child = child

        self.parent_ids = parent.id
        self.child_ids = parent.id

        self.fetch_rows = fetch_rows

        self.select: str = None
        self.where: str = None

    def load_parent(self, s_parent: M_Structure, s_child: M_Structure):
        get_entity_rows(
            m_entity=s_parent.node,
            column=self.parent_ids,
            value=self.get_node_values(self.child_ids, s_child.node),
            fetch_rows=1,
        )

    def load_childs(self, s_parent: M_Structure, s_child: M_Structure):
        get_entity_rows(
            m_entity=s_child.node,
            column=self.child_ids,
            value=self.get_node_values(self.parent_ids, s_parent.node),
            fetch_rows=self.fetch_rows,
            select=self.select,
            where=self.where,
        )

    def get_node_values(self, ids: list, ent: M_Entity):
        """
        docstring
        """
        lt = []
        for x in ids:
            lt.append(ent.row_dict[x])
        return lt
