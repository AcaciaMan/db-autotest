from db_autotest.m_lib.m_object.m_str_type_enum import M_StructureType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db_autotest.m_lib.m_object.m_relation import M_Relation
    from db_autotest.m_lib.m_object.m_entity import M_Entity

class M_Structure(object):
    """
    docstring
    """
    def __init__(self, m_entity: 'M_Entity', m_type: M_StructureType = M_StructureType.TOP):
        """
        docstring
        """
        self.i_row: int = None

        self.parent = []
        self.child = []

        self.node = m_entity
        self.m_type = m_type


    @property
    def m_type(self):
        """
        docstring
        """
        return self._m_type
    
    @m_type.setter
    def m_type(self, value):
        """
        docstring
        """
        self._m_type = value
        self.node.m_type = value

    def load_nodes(self):
        
        str1: M_Structure
        rel: M_Relation
        for str1, rel in self.parent:
            rel.load_parent(str1, self)
            str1.load_nodes()

        for str1, rel in self.child:
            rel.load_childs(self, str1)


        # create for each loaded child a new structure and load nodes for them
        new_child = []
        for str1, rel in self.child:
            for i, x in enumerate(str1.node.rows):
                str2 = M_Structure(str1.node, M_StructureType.CHILD)
                str2.i_row = i

                new_parent = []
                for str4, rel4 in str1.parent:
                    node5 = str4.node.copy_entity()
                    str5 = M_Structure(node5, M_StructureType.PARENT)
                    new_parent.append([str5, rel4])
                str2.parent = new_parent

                new_child5 = []
                for str4, rel4 in str1.child:
                    node5 = str4.node.copy_entity()
                    str5 = M_Structure(node5, M_StructureType.CHILD)
                    new_child5.append([str5, rel4])
                str2.child = new_child5

                new_child.append([str2, rel])

        self.child = new_child

        for str1, rel in self.child:
            str1.load_nodes()


    @property
    def node(self):
        """
        docstring
        """
        if self.i_row is None:
            return self._node
        else:
            self._node.i_row = self.i_row
            return self._node
        
    @node.setter
    def node(self, value):
        """
        docstring
        """
        self._node = value
        


