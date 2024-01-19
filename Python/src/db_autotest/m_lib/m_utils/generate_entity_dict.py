import sqlite3
from db_autotest.m_lib.m_config.config import M_Config

class GenerateEntityDict(object):
    """
    docstring
    """
    def __init__(self, path, entity_dict):
        """
        docstring
        """
        self.path = path
        self.entity_dict = entity_dict
        self.cur = None

    def __call__(self):
        """
        docstring
        """
        if self.path:
            self.delete_prev_entities()
            self.insert_entities()

        else:
            self.cur = M_Config.meta().cursor()
            self.load_db_meta_entities_dict()
            self.cur.close()

    def delete_prev_entities(self):
        """
        docstring
        """
        started = 'Generated Code Start'
        ended = 'Generated Code End'
        b_started = 0
        b_ended = 0

        try:
            with open(self.path, 'r+') as f:
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


    def insert_entities(self):
        """
        docstring
        """
        started = 'Generated Code Start'

        try:
            with open(self.path, 'r+') as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    f.write(i)

                    if started in i:
                        # select all tables
                        f.write(f'        self.d_m_entities = {self.entity_dict}\n')
                        f.write('\n')

                f.truncate()


        except Exception as e:
            print(e)

    def load_db_meta_entities_dict(self):
        """
        docstring
        """
        # load data
        # delete packages data from db
        # insert packages data
        d_c = self.load_from_meta_db()
        del_c = {}

        for k in d_c.keys():
            if k not in self.entity_dict:
                self.delete_m_entity(k)
                del_c[k] = True
            else:
                if not (d_c[k] == self.entity_dict[k]):
                    self.delete_m_entity(k)
                    del_c[k] = True

        for k in del_c.keys():
            d_c.pop(k)
            print('Deleted:',k)

        for k in self.entity_dict.keys():
            if k not in d_c:
                self.insert_m_entity(self.entity_dict[k])


    def load_from_meta_db(self):
        """
        docstring
        """
        conn = M_Config.meta(new=True)

        # Configure the connection to return rows as dictionaries
        conn.row_factory = sqlite3.Row

        # Create a cursor
        cur = conn.cursor()

        # Execute a SELECT query
        cur.execute("select * from m_entity")

        # Fetch all rows from the query
        rows = cur.fetchall()

        # Convert rows to dictionaries
        dicts = [dict(row) for row in rows]

        # Close the connection
        conn.close()

        d_c = {}
        for d in dicts:
            d.pop('M_ENTITY_ID')
            d_c[d['M_CLASS']] = d

        return d_c
    
    def insert_m_entity(self, data):
        """
        docstring
        """
         # Prepare the INSERT query
        query = f"INSERT INTO m_entity ({', '.join(data.keys())}) VALUES ({', '.join(['?' for _ in data])})"

        # Execute the INSERT query
        self.cur.execute(query, list(data.values()))

        # Commit the changes
        M_Config.meta().commit()

    def delete_m_entity(self, m_class):
        """
        docstring
        """
        # Prepare the INSERT query
        query = "delete from m_entity where m_class = ?"

        # Execute the INSERT query
        self.cur.execute(query, (m_class,))

        # Commit the changes
        M_Config.meta().commit()