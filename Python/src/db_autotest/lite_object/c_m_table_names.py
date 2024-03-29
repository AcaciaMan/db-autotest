from db_autotest.m_lib.m_object.m_object import M_Meta_DB_Decorator, M_Object_Decorator, M_Table_Decorator
from db_autotest.m_lib.m_table.m_table import m_column, m_object, m_object_detail
from db_autotest.m_lib.m_utils.m_entity_utils import add_db_code_alias
from db_autotest.lite_object.c_m_table import C_M_Table
import db_autotest.m_lib.m_config.config as cn

@M_Object_Decorator
@M_Meta_DB_Decorator
@M_Table_Decorator
class C_M_TableNames(C_M_Table):
    """
    docstring
    """
    def __init__(self):
        """
        docstring
        """
        super().__init__()

        #============================================ m_table ======================================================
        add_db_code_alias(self.t_m_table, '(select o.NAME from m_object o where t.M_OBJECT_ID = o.m_object_id) as table_name', 'table_name')

        self.t_m_table.row.c[cn.M_Config.main_env].append(self.t_m_table.aliases['table_name']) 

        row1 = []
        row1.append(self.t_m_table.aliases['table_name'])
        row1.append(m_object_detail().droped)        

        self.t_m_table.pretty_row = row1
        #============================================ m_object ======================================================
        row1 = []
        row1.append(m_object().schema)
        row1.append(m_object().name)

        self.t_m_object.pretty_row = row1

        #============================================ m_index ======================================================
        add_db_code_alias(self.t_m_index, '(select o.NAME from m_object o where t.M_OBJECT_ID = o.m_object_id) as index_name', 'index_name')

        self.t_m_index.row.c[cn.M_Config.main_env].append(self.t_m_index.aliases['index_name']) 

        row1 = []
        row1.append(self.t_m_index.aliases['index_name'])
        row1.append(m_object_detail().m_unique)   
        row1.append(m_object_detail().status)   
        row1.append(m_object_detail().enabled)   
        row1.append(m_object_detail().droped)        

        self.t_m_index.pretty_row = row1

        #============================================ m_column ======================================================
        add_db_code_alias(self.t_m_column, '(select o.NAME from m_object o where t.M_COLUMN_OBJ_ID = o.M_OBJECT_ID) as column_name', 'column_name')

        self.t_m_column.row.c[cn.M_Config.main_env].append(self.t_m_column.aliases['column_name']) 

        row1 = []
        row1.append(self.t_m_column.aliases['column_name'])
        row1.append(m_column().sort)
        row1.append(m_column().type)
        row1.append(m_column().pk)


        self.t_m_column.pretty_row = row1

        #============================================ m_idx_column ======================================================
        add_db_code_alias(self.t_m_idx_column, '(select o.NAME from m_object o where t.M_COLUMN_OBJ_ID = o.M_OBJECT_ID) as column_name', 'column_name')

        self.t_m_idx_column.row.c[cn.M_Config.main_env].append(self.t_m_idx_column.aliases['column_name']) 

        row1 = []
        row1.append(self.t_m_idx_column.aliases['column_name'])
        row1.append(m_column().sort)

        self.t_m_idx_column.pretty_row = row1


        




