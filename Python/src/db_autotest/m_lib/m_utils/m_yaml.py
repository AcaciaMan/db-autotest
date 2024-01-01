from typing import TYPE_CHECKING

from db_autotest.m_lib.m_object.m_str_type_enum import M_StructureType
if TYPE_CHECKING:
    from db_autotest.m_lib.m_object.m_structure import M_Structure


class M_Yaml(object):
    """
    docstring
    """
    def __init__(self):
        """
        docstring
        """
        self.s: str

    def get_yaml(self, m_structure: 'M_Structure'):
        """
        Get node entity
        Get parent nodes
        Get child nodes
            1 diffs from many 
        """
        self.s = m_structure.node.__str__()

        s8 = self.get_nodes(m_structure, 0)

        if s8 is not None:
            self.s = self.s + '\n' + s8

        return self.s


    
    def get_nodes(self, m_structure: 'M_Structure', level: int):
        """
        docstring
        """
        if len(m_structure.parent)>0 or len(m_structure.child)>0:
            s4 = "".join(['  ']*level)

            s7 = ''

            if m_structure.m_type == M_StructureType.CHILD:
                s7= 'c_'

            if m_structure.m_type == M_StructureType.PARENT:
                s7= 'p_'

            s1 = s4 + s7+ m_structure.node.name + '_nodes: [\n'

            s2 = self.get_parent_child_nodes(m_structure, level+1)

            s3 = '\n' +s4+ ']'

            return s1 +s2 +s3
        
        return None


    def get_parent_child_nodes(self, m_structure: 'M_Structure', level):
        """
        p_object: {'object_id': 4, 'schema': 4},
        c_columns: [
            c_column: {'name': 'col1', 'seq_no': 'col2'},
            c_column_nodes: [
                p_type: {'name': 'Varchar2'}
            ],
            c_column: {'name': 'col2'}
        ]
        """
        s4 = "".join(['  ']*level)

        s1: str = ''
        structure: M_Structure
        i=0
        for structure, rel in m_structure.parent:
            if structure.node.row_data is not None:
                s1 = s1 + s4 + 'p_' + structure.node.__str__() + ',\n'
                s8 = self.get_nodes(structure, level)
                if s8 is not None:
                    s1 = s1 + s8+ ',\n'
                i=i+1


        # check if child has rows
        for structure, rel in m_structure.child:
            if structure.node.row_data is not None:
                s1 = s1 + s4 + 'c_' + structure.node.__str__() + ',\n'
                s8 = self.get_nodes(structure, level)
                if s8 is not None:
                    s1 = s1 + s8+ ',\n'
                i=i+1

        if i>0:
            s1=s1[0:-2]

        return s1

    
