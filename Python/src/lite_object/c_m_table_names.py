from src.lib.m_table.m_table import m_column
from src.lib.utils.m_entity_utils import add_db_code_alias, apply_to_all_env
from src.lite_object.c_m_table import C_M_Table


class C_M_TableNames(C_M_Table):
    """
    docstring
    """
    def __init__(self):
        """
        docstring
        """
        super().__init__()

        add_db_code_alias(self.t_m_column, '(select o.NAME from m_object o where t.M_COLUMN_OBJ_ID = o.M_OBJECT_ID) as column_name', 'column_name')

        row1 = []
        row1.append(self.t_m_column.aliases['column_name'])
        row1.append(m_column().sort)
        row1.append(m_column().type)


        apply_to_all_env(self.t_m_column, row1)


        add_db_code_alias(self.t_m_idx_column, '(select o.NAME from m_object o where t.M_COLUMN_OBJ_ID = o.M_OBJECT_ID) as column_name', 'column_name')

        row1 = []
        row1.append(self.t_m_idx_column.aliases['column_name'])
        row1.append(m_column().sort)

        apply_to_all_env(self.t_m_idx_column, row1)


        




