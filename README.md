# db-autotest
DB Database test automation. This python package allows to create database object structure and load data from database.

One further option is to print, save data as YAML file, another is to use retrieved object in data comparissons or new database object creation.

AcaciaMan/db-autotest-vscode is related repository for UI (User Interface) part in Microsoft Visual Studio Code as extension.

## DB structure as object in Python
Better explanation is code example from [c_m_table.py](https://github.com/AcaciaMan/db-autotest/blob/main/Python/src/db_autotest/lite_object/c_m_table.py).


```python

class C_M_Table(object):

    def __init__(self):

        # ==================================== m_table ===============================
        self.t_m_table = M_Entity(m_object_detail(), m_object_detail_r(), name='table')
        
        # ==================================== m_object ===============================
        self.t_m_object = M_Entity(m_object(), m_object_r(), name='object')

        self.r_m_object_table = M_Relation(self.t_m_object, self.t_m_table)
        self.s_m_object = M_Structure(self.t_m_object, M_StructureType.PARENT)

        # ==================================== m_column ===============================
        self.t_m_column = M_Entity(m_column(), m_column_r(), name='column')
        self.t_m_column.sortFunc = columnSortFunc.__get__(self.t_m_column)

        self.r_m_table_column = M_Relation(self.t_m_table, self.t_m_column)
        self.s_m_column = M_Structure(self.t_m_column, M_StructureType.CHILD)

        # ==================================== m_index ===============================
        self.t_m_index = M_Entity(m_object_detail(), m_object_detail_r(), name='index')

        self.r_m_table_index = M_Relation(self.t_m_table, self.t_m_index)
        self.r_m_table_index.parent_ids = [m_object_detail().m_object_id, m_object_detail().m_version_id]
        self.r_m_table_index.child_ids = [m_object_detail().idx_table_id, m_object_detail().m_version_id]
        self.s_m_index = M_Structure(self.t_m_index, M_StructureType.CHILD)

        # ==================================== m_idx_column ===============================
        self.t_m_idx_column = M_Entity(m_column(), m_column_r(), name='idx_column')
        self.t_m_idx_column.sortFunc = columnSortFunc.__get__(self.t_m_idx_column)

        self.r_m_idx_column = M_Relation(self.t_m_index, self.t_m_idx_column)
        self.s_m_idx_column = M_Structure(self.t_m_idx_column, M_StructureType.CHILD)        
        self.s_m_index.child.append([self.s_m_idx_column, self.r_m_idx_column])

        # ==================================== s_m_table ===============================
        self.s_m_table = M_Structure(self.t_m_table)
        self.s_m_table.parent.append([self.s_m_object, self.r_m_object_table])
        self.s_m_table.child.append([self.s_m_column, self.r_m_table_column])
        self.s_m_table.child.append([self.s_m_index, self.r_m_table_index])

        self.c_main = M_Class(self.s_m_table)


def columnSortFunc(self, e):
    return e[get_column_i(self, m_column().sort)]

    
```

## Output as YAML file
Output can be saved as YAML file [test.yaml](https://github.com/AcaciaMan/db-autotest/blob/main/Python/tests/yaml/test.yaml)


```yaml
table: {'m_object_detail_id': 4, 'm_object_id': 4, 'm_version_id': 1, 'idx_table_id': None, 'm_unique': 0, 'status': 'VALID', 'enabled': 1, 'droped': 0}

table_nodes: [

  p_object: {'m_object_id': 4, 'schema': 'db', 'name': 'm_column', 'type': 'TABLE', 'create_date': 1703982912},
  c_column: {'m_column_id': 11, 'm_object_detail_id': 4, 'm_column_obj_id': 24, 'sort': 0, 'type': 'INTEGER'},
  c_column: {'m_column_id': 12, 'm_object_detail_id': 4, 'm_column_obj_id': 25, 'sort': 1, 'type': 'INTEGER'},
  c_column: {'m_column_id': 13, 'm_object_detail_id': 4, 'm_column_obj_id': 26, 'sort': 2, 'type': 'INTEGER'},
  c_column: {'m_column_id': 14, 'm_object_detail_id': 4, 'm_column_obj_id': 27, 'sort': 3, 'type': 'INTEGER'},
  c_column: {'m_column_id': 15, 'm_object_detail_id': 4, 'm_column_obj_id': 22, 'sort': 4, 'type': 'TEXT'},
  c_index: {'m_object_detail_id': 10, 'm_object_id': 10, 'm_version_id': 1, 'idx_table_id': 4, 'm_unique': 1, 'status': 'VALID', 'enabled': 1, 'droped': 0},
  c_index_nodes: [
    c_idx_column: {'m_column_id': 31, 'm_object_detail_id': 10, 'm_column_obj_id': 25, 'sort': 0, 'type': None},
    c_idx_column: {'m_column_id': 32, 'm_object_detail_id': 10, 'm_column_obj_id': 26, 'sort': 1, 'type': None},
    c_idx_column: {'m_column_id': 33, 'm_object_detail_id': 10, 'm_column_obj_id': 27, 'sort': 2, 'type': None}
  ],
  c_index: {'m_object_detail_id': 11, 'm_object_id': 11, 'm_version_id': 1, 'idx_table_id': 4, 'm_unique': 0, 'status': 'VALID', 'enabled': 1, 'droped': 0},
  c_index_nodes: [
    c_idx_column: {'m_column_id': 34, 'm_object_detail_id': 11, 'm_column_obj_id': 26, 'sort': 0, 'type': None}
  ]
]

```

## More examples

More examples can be found in files [c_m_table_names.py](https://github.com/AcaciaMan/db-autotest/blob/main/Python/src/db_autotest/lite_object/c_m_table_names.py) and [test_names.yaml](https://github.com/AcaciaMan/db-autotest/blob/main/Python/tests/yaml/test_names.yaml)

## Environment setup
Docs folder contains [initial setup description](https://github.com/AcaciaMan/db-autotest/blob/main/Docs/python_setup.md) and [SQLite database for db metadata](https://github.com/AcaciaMan/db-autotest/blob/main/Docs/m_sqlite.db).
