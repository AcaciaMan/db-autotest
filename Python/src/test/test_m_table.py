import unittest
from src.m_lib.m_table import m_table as t  # noqa: E402
from src.m_lib.m_table import m_row as r

class Test_M_Table(unittest.TestCase):

    def test_access(self):
        d = t.dual()
        print(type(d).__name__)
        print(d.dummy)

        row = r.dual_r()
        print(row.c['dev'])

        '''
        v = t.m_version
        print(v.m_version_id)
        print(v.r[v.m_version_id])
        '''

        #v = t.m_version()
        #print(v.load_date)

if __name__ == '__main__':
    unittest.main()