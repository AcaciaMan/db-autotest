import json
from db_autotest.m_lib.m_object.m_str_type_enum import M_StructureType
from db_autotest.m_lib.m_object.m_structure import M_Structure

class M_JSON(object):
    """
    docstring
    """
    def __init__(self):
        """
        docstring
        """
        self.obj = {}
        self.s: str

    def get_json(self, m_structure: M_Structure):
        """
        Get node entity
        Get parent nodes
        Get child nodes
            1 diffs from many 
        """
        self.obj[m_structure.node.name] = m_structure.node.getPrettyObject()
        self.get_nodes(self.obj, m_structure, 0)
        return self.obj


    
    def get_nodes(self, n_obj, m_structure: 'M_Structure', level: int):
        """
        docstring
        """
        if len(m_structure.parent)>0 or len(m_structure.child)>0:
            s7 = ''
            if m_structure.m_type == M_StructureType.CHILD:
                s7= 'c_'
            if m_structure.m_type == M_StructureType.PARENT:
                s7= 'p_'
            l_n = []
            n_obj[s7+ m_structure.node.name + '_nodes'] = l_n
            self.get_parent_child_nodes(l_n, m_structure, level+1)

            return n_obj
        
        return None


    def get_parent_child_nodes(self, l_n, m_structure: M_Structure, level):
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

        structure: M_Structure
        for structure, rel in m_structure.parent:
            if structure.node.row_data is not None:
                d_o = {}
                d_o['p_' + structure.node.name] = structure.node.getPrettyObject()
                l_n.append(d_o)
                self.get_nodes(d_o, structure, level)


        # check if child has rows
        for structure, rel in m_structure.child:
            if structure.node.row_data is not None:
                d_o = {}
                d_o['c_' + structure.node.name] = structure.node.getPrettyObject()
                l_n.append(d_o)
                self.get_nodes(d_o, structure, level)

        return l_n

    def stringify(self, level = 0):
        """
{
 "table": {"table_name": "m_column", "droped": 0},
 "table_nodes": [
    {"p_object": {"schema": "db", "name": "m_column"}},
    {"c_column": {"column_name": "m_column_id", "sort": 0, "type": "INTEGER", "pk": null}},
    {"c_column": {"column_name": "m_object_detail_id", "sort": 1, "type": "INTEGER", "pk": null}},
    {"c_column": {"column_name": "m_column_obj_id", "sort": 2, "type": "INTEGER", "pk": null}},
    {"c_column": {"column_name": "sort", "sort": 3, "type": "INTEGER", "pk": null}},
    {"c_column": {"column_name": "type", "sort": 4, "type": "TEXT", "pk": null}},
    {"c_index": {"index_name": "m_column_idx", "m_unique": 1, "status": "VALID", "enabled": 1, "droped": 0}},
    {"c_index_nodes": [
        {"c_idx_column": {"column_name": "m_object_detail_id", "sort": 0}},
        {"c_idx_column": {"column_name": "m_column_obj_id", "sort": 1}},
        {"c_idx_column": {"column_name": "sort", "sort": 2}}
        ]},
    {"c_index": {"index_name": "m_column_obj_idx", "m_unique": 0, "status": "VALID", "enabled": 1, "droped": 0}},
    {"c_index_nodes": [
        {"c_idx_column": {"column_name": "m_column_obj_id", "sort": 0}}
        ]}
    ]
}
        """
        s4 = "".join(['    ']*(level+1))
        self.s = '{\n'

        for x in self.obj.keys():
            if not isinstance(self.obj[x], list):
                self.s = self.s + ' "' + x + '": ' + json.dumps(self.obj[x]) + ',\n'
            else:
                self.s = self.s + ' "' + x + '": [\n'
                self.s = self.s + self.add_parent_child_nodes(self.obj[x], level+1)
                self.s = self.s + s4 + '],\n'

        if len(self.s) > 2:
            self.s = self.s[0:-2] + '\n' # remove last comma

        self.s = self.s + '}\n'
        return self.s


    def add_parent_child_nodes(self, objList, level):
        """
        docstring
        """
        s5 = "".join(['    ']*(level))
        s4 = "".join(['    ']*(level+1))

        s7 = ''
        for x in objList:
            for y in x.keys():
                if not isinstance(x[y], list):
                    s7 = s7 + s5 + '{"' + y + '": ' + json.dumps(x[y]) + '},\n'
                else:
                    s7 = s7 + s5 + '{"' + y + '": [\n'
                    s7 = s7 + self.add_parent_child_nodes(x[y], level+1)
                    s7 = s7 + s4 + ']},\n'


        if len(s7) > 2:
            s7 = s7[0:-2] + '\n' # remove last comma

        return s7

