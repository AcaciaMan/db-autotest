from db_autotest.m_lib.m_table.m_table import M_Table  # noqa: F401

# ===================== Generated Code Start ======================================================
class m_person(M_Table):
    def __init__(self):
        super().__init__()
        self.m_person_id = 'm_person_id'
        self.owner = 'owner'
        self.name = 'name'

class m_organization(M_Table):
    def __init__(self):
        super().__init__()
        self.m_organization_id = 'm_organization_id'
        self.parent_org_id = 'parent_org_id'
        self.name = 'name'

class m_employee(M_Table):
    def __init__(self):
        super().__init__()
        self.m_employee_id = 'm_employee_id'
        self.m_person_id = 'm_person_id'
        self.manager = 'manager'
        self.m_organization_id = 'm_organization_id'

# ======================= Generated Code End =======================================================
