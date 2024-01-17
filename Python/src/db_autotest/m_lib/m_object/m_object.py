from db_autotest.m_lib.m_config.config import M_Config
from db_autotest.m_lib.m_object.m_class import M_Class


def M_Object_Decorator(cls):
    return cls

def M_Table_Decorator(cls):
    return cls

def M_Meta_DB_Decorator(cls):
    return cls

class M_Object(object):
    """
    docstring
    """
    def __init__(self):
        """
        docstring
        """
        self.main_class: M_Class = None


    def __call__(self, m_id: list, con = M_Config.con):
        """
        Load main class
        """
        self.main_class.load(m_id=m_id, con=con)
