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
        self.m_env_id = 'm_env_id'
        self.name = 'name'

class m_version(M_Table):
    def __init__(self):
        super().__init__()
        self.m_env_id = 'm_env_id'
        self.load_date = 'load_date'
        self.m_version_id = 'm_version_id'

class m_object(M_Table):
    def __init__(self):
        super().__init__()
        self.schema = 'schema'
        self.create_date = 'create_date'
        self.m_object_id = 'm_object_id'
        self.type = 'type'
        self.name = 'name'

class m_object_detail(M_Table):
    def __init__(self):
        super().__init__()
        self.m_unique = 'm_unique'
        self.droped = 'droped'
        self.m_object_id = 'm_object_id'
        self.idx_table_id = 'idx_table_id'
        self.enabled = 'enabled'
        self.m_version_id = 'm_version_id'
        self.status = 'status'
        self.m_object_detail_id = 'm_object_detail_id'

class m_column(M_Table):
    def __init__(self):
        super().__init__()
        self.m_column_id = 'm_column_id'
        self.sort = 'sort'
        self.m_column_obj_id = 'm_column_obj_id'
        self.m_object_detail_id = 'm_object_detail_id'
        self.type = 'type'

# ===================== Generated Code End   ======================================================