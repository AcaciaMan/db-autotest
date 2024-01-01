class M_Table(object):
    """
    docstring
    """
    def __init__(self):
        """
        docstring
        """
        pass

class dual(M_Table):
    def __init__(self):
        super().__init__()
        self.dummy='dummy'

# TODO load primary keys from meta data

# ===================== Generated Code Start ======================================================
class m_env(M_Table):
    def __init__(self):
        super().__init__()
        self.name = 'name'
        self.m_env_id = 'm_env_id'

class m_version(M_Table):
    def __init__(self):
        super().__init__()
        self.m_version_id = 'm_version_id'
        self.m_env_id = 'm_env_id'
        self.load_date = 'load_date'

class m_object(M_Table):
    def __init__(self):
        super().__init__()
        self.m_object_id = 'm_object_id'
        self.schema = 'schema'
        self.name = 'name'
        self.create_date = 'create_date'
        self.type = 'type'

class m_column(M_Table):
    def __init__(self):
        super().__init__()
        self.m_column_id = 'm_column_id'
        self.sort = 'sort'
        self.m_column_obj_id = 'm_column_obj_id'
        self.m_object_detail_id = 'm_object_detail_id'
        self.type = 'type'

class m_object_detail(M_Table):
    def __init__(self):
        super().__init__()
        self.m_unique = 'm_unique'
        self.m_object_id = 'm_object_id'
        self.enabled = 'enabled'
        self.idx_table_id = 'idx_table_id'
        self.droped = 'droped'
        self.m_version_id = 'm_version_id'
        self.status = 'status'
        self.m_object_detail_id = 'm_object_detail_id'

# ======================= Generated Code End =======================================================