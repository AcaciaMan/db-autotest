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

    def __call__(self):
        """
        docstring
        """
        self.delete_prev_entities()
        self.insert_entities()


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
