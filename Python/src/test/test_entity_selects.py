import unittest
from src.lib.m_object.m_entity import M_Entity
from src.lib.m_table.m_row import m_object_detail_r
from src.lib.m_table.m_table import m_object_detail
from src.lib.utils.m_entity_selects import get_entity_rows

class TestSelects(unittest.TestCase):

    def testTableLoad(self):
        print("Started")
        #lt.LoadTables().load()
        lt = M_Entity(m_object_detail(), m_object_detail_r())
        get_entity_rows(lt, [m_object_detail().m_object_detail_id, m_object_detail().m_object_id], [179, 4] )
        print(lt.row_dict)
        #LoadVersion().load()

if __name__ == '__main__':
    unittest.main()