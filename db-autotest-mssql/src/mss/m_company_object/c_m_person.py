from db_autotest.m_lib.m_object.m_class import M_Class
from db_autotest.m_lib.m_object.m_entity import M_Entity
from db_autotest.m_lib.m_object.m_relation import M_Relation
from db_autotest.m_lib.m_object.m_str_type_enum import M_StructureType
from db_autotest.m_lib.m_object.m_structure import M_Structure
from mss.m_lib.app_table.app_row import m_employee_r, m_person_r
from mss.m_lib.app_table.app_table import m_employee, m_person

class C_M_Person(object):
    """
    docstring
    """
    def __init__(self):
        """
        docstring
        """
        # ============================ m_person =================================
        self.t_m_person = M_Entity(m_person(), m_person_r(), name = 'person')

        # =========================== m_employee ================================
        self.t_m_employee = M_Entity(m_employee(), m_employee_r(), name = 'employee')

        self.r_m_person_employee = M_Relation(self.t_m_person, self.t_m_employee)
        self.s_m_employee = M_Structure(self.t_m_employee, M_StructureType.CHILD)

        # =========================== s_m_person ================================
        self.s_m_person = M_Structure(self.t_m_person)
        self.s_m_person.child.append([self.s_m_employee, self.r_m_person_employee])

        self.c_main = M_Class(self.s_m_person)
