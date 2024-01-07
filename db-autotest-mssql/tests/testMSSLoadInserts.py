from mss.load_mssql_meta.mss_load_version_tables import MSS_LoadVersionTables
from mss.m_lib.m_utils.mss_load_inserts import MSS_LoadInserts


MSS_LoadInserts.insert_tables()
MSS_LoadInserts.insert_indexes()
MSS_LoadInserts.insert_columns()
inserted_id = MSS_LoadInserts.insert_version()
v_tables = MSS_LoadVersionTables(inserted_id)
v_tables().insert_into_meta_db()
v_tables().insert_columns()

