import unittest

from src.lib.m_object.m_str_type_enum import M_StructureType

class Test_M_Dict(unittest.TestCase):

    def test_access(self):
        d = dict()

        print(d)

    def test_list(self):
        """
        docstring
        """
        n = 'string'
        l2 = [['something', n], ['new', 1], ['enabled', None]]
        s = '{'

        i = 0

        for x1 in l2:
            s = s + ': '.join(map(str, map(lambda x: f"'{x}'" if isinstance(x, str) else x, x1))) + ', '
            i=i+1
        
        if i>0:
            s= s[0:-2]

        s = s + '}'    

        print(s)

    def test_enum(self):
        """
        docstring
        """
        top_e = M_StructureType.TOP


        print(top_e)

        if top_e == M_StructureType.TOP:
            print(top_e == M_StructureType.TOP)


if __name__ == '__main__':
    unittest.main()