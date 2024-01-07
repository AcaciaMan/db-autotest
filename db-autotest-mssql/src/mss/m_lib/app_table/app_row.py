from db_autotest.m_lib.m_table.m_row import M_Row  # noqa: F401

# ===================== Generated Code Start ======================================================
class m_person_r(M_Row):
    def __init__(self):
        super().__init__()
        self.c['dev'] = ['m_person_id','name','owner']
        self.pk['dev'] = ['m_person_id']

class m_organization_r(M_Row):
    def __init__(self):
        super().__init__()
        self.c['dev'] = ['m_organization_id','name','parent_org_id']
        self.pk['dev'] = ['m_organization_id']

class m_employee_r(M_Row):
    def __init__(self):
        super().__init__()
        self.c['dev'] = ['m_employee_id','m_person_id','m_organization_id','manager']
        self.pk['dev'] = ['m_employee_id']

# ======================= Generated Code End =======================================================
