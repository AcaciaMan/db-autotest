import src.db_autotest.m_lib.config.config as cn

class GetValues(object):
    """
    docstring
    """
    @staticmethod
    def get_m_env_id():
        cur = cn.meta().cursor()

        cur.execute(
        '''
        select m.M_ENV_ID from m_env m where lower(m.NAME) = lower(?)
        ''', (cn.Config.main_env,)
        )

        r = cur.fetchone()
        print("env id", r[0])
        cur.close()
        return r[0]   
    
    @staticmethod
    def get_all_tables():
        cur = cn.meta().cursor()

        cur.execute(
        '''
        select m_object_id, name from m_object where type = 'TABLE'
        '''
        )

        r = cur.fetchall()
        cur.close()
        return r 
     
    @staticmethod
    def get_all_indexes():
        """
        Select all indexes
        """
        
        cur = cn.meta().cursor()

        cur.execute(
            '''
            select m_object_id, name from m_object where type = 'INDEX'
            ''')

        row = cur.fetchall()

        cur.close()

        return row
    
    @staticmethod
    def get_last_m_object_detail_id(m_object_id, env_name):
        """
        Select last_m_object_detail_id
        """
        
        cur = cn.meta().cursor()

        cur.execute(
            '''
            select m.m_object_detail_id 
            from m_object_detail m, m_version v, m_env e 
            where m.m_object_id = ?
            and m.m_version_id = v.m_version_id
            and v.m_env_id = e.m_env_id
            and e.name = ?
            order by v.load_date desc
            ''', (m_object_id, env_name))

        row = cur.fetchone()

        cur.close()

        m_object_detail_id = row[0] if row else None

        return m_object_detail_id
    
    @staticmethod
    def get_columns(m_object_detail_id):
        """
        Select columns
        """
        
        cur = cn.meta().cursor()

        cur.execute(
            '''
            select o.m_object_id, o.name 
            from m_column m, m_object o 
            where m.m_object_detail_id = ?
            and o.m_object_id =  m.m_column_obj_id 
            and lower(m.type) not like '%lob%' 
            order by sort
            ''', (m_object_detail_id, ))

        row = cur.fetchall()

        cur.close()

        return row