# Get tables module
# Open w module
# find Generate Code Start
# delete till Generate Code End
# insert new table classes
#   add attributes as columns sorted
#   add dict for each env as list of columns what are not LOB
#   add dict of columns

from db_autotest.m_lib.m_config.config  import M_Config as cn
from db_autotest.m_lib.m_utils.selects import GetValues

class GenerateTabCols(object):
    """
    docstring
    """
    @staticmethod
    def delete_prev_tables():
        """
        docstring
        """
        path_tabs = cn.config.get('DEFAULT','tables_module')

        started = 'Generated Code Start'
        ended = 'Generated Code End'
        b_started = 0
        b_ended = 0

        try:
            with open(path_tabs, 'r+') as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if ended in i:
                        b_ended = 1

                    if not(b_started == 1 and b_ended == 0):
                        f.write(i)


                    if started in i:
                        b_started = 1

                f.truncate()
        except Exception as e:
            print(e)        


    @staticmethod
    def insert_tables():
        """
        docstring
        """
        path_tabs = cn.config.get('DEFAULT','tables_module')

        started = 'Generated Code Start'

        cur = cn.meta().cursor()

        try:
            with open(path_tabs, 'r+') as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    f.write(i)

                    if started in i:
                        # select all tables
                        all_tables = GetValues.get_all_tables()

                        for t_id, t_name in all_tables:

                            '''
                            class dual(M_Table):
                                def __init__(self):
                                    super().__init__()
                                    self.dummy='dummy'
                            '''

                            f.write('class ' + t_name + '(M_Table):\n')
                            f.write('    def __init__(self):\n')
                            f.write('        super().__init__()\n')

                            s = set()

                            # find for each env last list of columns
                            for x in cn.env_dict.keys():
                                m_object_detail_id = GetValues.get_last_m_object_detail_id(t_id, x)
                                if m_object_detail_id is not None:
                                    all_cols = GetValues.get_columns(m_object_detail_id)
                                    for col_id, col_name in all_cols:
                                        s.add(col_name)

                            for si in s:
                                f.write("        self."+si+" = '" + si+ "'" + '\n')

                            f.write('\n')

                f.truncate()

            cur.close()

        except Exception as e:
            print(e)


    @staticmethod
    def delete_prev_rows():
        """
        docstring
        """
        path_tabs = cn.config.get('DEFAULT','rows_module')

        started = 'Generated Code Start'
        ended = 'Generated Code End'
        b_started = 0
        b_ended = 0

        try:
            with open(path_tabs, 'r+') as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if ended in i:
                        b_ended = 1

                    if not(b_started == 1 and b_ended == 0):
                        f.write(i)


                    if started in i:
                        b_started = 1

                f.truncate()
        except Exception as e:
            print(e)   

    @staticmethod
    def insert_rows():
        """
        docstring
        """
        path_tabs = cn.config.get('DEFAULT','rows_module')

        started = 'Generated Code Start'

        cur = cn.meta().cursor()

        try:
            with open(path_tabs, 'r+') as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    f.write(i)

                    if started in i:
                        # select all tables
                        all_tables = GetValues.get_all_tables()
                        '''
class dual_r(M_Row):
    def __init__(self):
        super().__init__()
        self.c['dev'] = ['dummy']
        self.c['tst'] = ['dummy']
        self.pk['dev'] = ['dummy']
        self.pk['tst'] = ['dummy']         
                        '''

                        for t_id, t_name in all_tables:

                            f.write('class ' + t_name + '_r(M_Row):\n')
                            f.write('    def __init__(self):\n')
                            f.write('        super().__init__()\n')

                            # find for each env last list of columns
                            for x in cn.env_dict.keys():
                                l_c = []
                                l_pk = []
                                m_object_detail_id = GetValues.get_last_m_object_detail_id(t_id, x)
                                if m_object_detail_id is not None:
                                    all_cols = GetValues.get_columns(m_object_detail_id)
                                    for col_id, col_name in all_cols:
                                        l_c.append("'" + col_name + "'")

                                    f.write("        self.c['"+ x +"'] = [" + ','.join(l_c) + "]\n")

                                    all_cols = GetValues.get_pk_columns(m_object_detail_id)
                                    for col_name in all_cols:
                                        l_pk.append("'" + col_name[0] + "'")

                                    f.write("        self.pk['"+ x +"'] = [" + ','.join(l_pk) + "]\n")

                            f.write('\n')

                f.truncate()

            cur.close()

        except Exception as e:
            print(e)
