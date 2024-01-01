import src.db_autotest.m_lib.config.config as cn
from src.db_autotest.m_lib.m_object.m_entity import M_Entity
from src.db_autotest.m_lib.utils.m_entity_utils import fill_entity_dict


def get_entity_rows(
    m_entity: M_Entity,
    column,
    value,
    env=cn.Config.main_env,
    fetch_rows=cn.Config.config.get('DEFAULT', 'fetch_child_rows'),    
    select: str = None,
    where: str = None,
):
    """
    docstring
    """
    if select is None:
        select = "select "

    if where is None:
        where = " where 1=1 "

        for x in column:
            where = where + " and " + x + " = ?"

    cur = cn.con().cursor()

    m_entity.row_cols = m_entity.row.c[env]

    cols = ",".join(m_entity.row_cols)

    s = select + cols + " from " + type(m_entity.table).__name__ + " t " + where

    cur.execute(s, value)

    if fetch_rows == 1:
        m_entity.row_data = cur.fetchone()
        fill_entity_dict(m_entity, env)
    else:
        m_entity.rows = cur.fetchmany(fetch_rows)
    cur.close()

