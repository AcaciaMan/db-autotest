from typing import TYPE_CHECKING
from db_autotest.m_lib.m_config.config import M_Config

if TYPE_CHECKING:
    from db_autotest.m_lib.m_object.m_entity import M_Entity


def fill_entity_dict(m_entity: 'M_Entity', env=M_Config.main_env):
    """
    docstring
    """
    for i, x in enumerate(m_entity.row_cols):
        m_entity.row_dict[x] = m_entity.row_data[i]

def get_column_i(m_entity: 'M_Entity', column: str, env=M_Config.main_env) -> int:
    """
    docstring
    """
    for i, x in enumerate(m_entity.row_cols):
        if x==column:
            return i
    return None

def add_db_code_alias(m_entity: 'M_Entity', db_code: str, alias: str):
    m_entity.aliases[alias] = db_code
    m_entity.db_code[db_code] = alias


