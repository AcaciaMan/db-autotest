class M_Row(object):
    """
    docstring
    """
    def __init__(self):
        """
        docstring
        """
        self.c={}

class dual_r(M_Row):
    def __init__(self):
        super().__init__()
        self.c['dev'] = ['dummy']
        self.c['tst'] = ['dummy']

# ===================== Generated Code Start ======================================================
class m_env_r(M_Row):
    def __init__(self):
        super().__init__()
        self.c['dev'] = ['m_env_id','name']

class m_version_r(M_Row):
    def __init__(self):
        super().__init__()
        self.c['dev'] = ['m_version_id','m_env_id','load_date']

class m_object_r(M_Row):
    def __init__(self):
        super().__init__()
        self.c['dev'] = ['m_object_id','schema','name','type','create_date']

class m_column_r(M_Row):
    def __init__(self):
        super().__init__()
        self.c['dev'] = ['m_column_id','m_object_detail_id','m_column_obj_id','sort','type']

class m_object_detail_r(M_Row):
    def __init__(self):
        super().__init__()
        self.c['dev'] = ['m_object_detail_id','m_object_id','m_version_id','idx_table_id','m_unique','status','enabled','droped']

# ======================= Generated Code End =======================================================