from db_autotest.m_lib.m_object.m_class import M_Class
from db_autotest.m_lib.m_object.m_entity import M_Entity
from db_autotest.m_lib.m_object.m_relation import M_Relation
from db_autotest.m_lib.m_object.m_str_type_enum import M_StructureType
from db_autotest.m_lib.m_object.m_structure import M_Structure
from db_autotest.m_lib.m_table.m_row import m_column_r, m_object_detail_r, m_object_r
from db_autotest.m_lib.m_table.m_table import m_column, m_object, m_object_detail
from db_autotest.m_lib.m_utils.m_entity_utils import get_column_i


class C_M_Table(object):
    """
    docstring
    """
    def __init__(self):
        """
        docstring
        """
        # ==================================== m_table ===============================
        self.t_m_table = M_Entity(m_object_detail(), m_object_detail_r(), name='table')
        
        # ==================================== m_object ===============================
        self.t_m_object = M_Entity(m_object(), m_object_r(), name='object')

        self.r_m_object_table = M_Relation(self.t_m_object, self.t_m_table)
        self.s_m_object = M_Structure(self.t_m_object, M_StructureType.PARENT)

        # ==================================== m_column ===============================
        self.t_m_column = M_Entity(m_column(), m_column_r(), name='column')
        self.t_m_column.sortFunc = columnSortFunc.__get__(self.t_m_column)

        self.r_m_table_column = M_Relation(self.t_m_table, self.t_m_column)
        self.s_m_column = M_Structure(self.t_m_column, M_StructureType.CHILD)

        # ==================================== m_index ===============================
        self.t_m_index = M_Entity(m_object_detail(), m_object_detail_r(), name='index')

        self.r_m_table_index = M_Relation(self.t_m_table, self.t_m_index)
        self.r_m_table_index.parent_ids = [m_object_detail().m_object_id, m_object_detail().m_version_id]
        self.r_m_table_index.child_ids = [m_object_detail().idx_table_id, m_object_detail().m_version_id]
        self.s_m_index = M_Structure(self.t_m_index, M_StructureType.CHILD)

        # ==================================== m_idx_column ===============================
        self.t_m_idx_column = M_Entity(m_column(), m_column_r(), name='idx_column')
        self.t_m_idx_column.sortFunc = columnSortFunc.__get__(self.t_m_idx_column)

        self.r_m_idx_column = M_Relation(self.t_m_index, self.t_m_idx_column)
        self.s_m_idx_column = M_Structure(self.t_m_idx_column, M_StructureType.CHILD)        
        self.s_m_index.child.append([self.s_m_idx_column, self.r_m_idx_column])

        # ==================================== s_m_table ===============================
        self.s_m_table = M_Structure(self.t_m_table)
        self.s_m_table.parent.append([self.s_m_object, self.r_m_object_table])
        self.s_m_table.child.append([self.s_m_column, self.r_m_table_column])
        self.s_m_table.child.append([self.s_m_index, self.r_m_table_index])

        self.c_main = M_Class(self.s_m_table)


def columnSortFunc(self, e):
    return e[get_column_i(self, m_column().sort)]