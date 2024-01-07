from mss.load_mssql_meta.mss_load_version_indexes import MSS_LoadVersionIndexes
from mss.load_mssql_meta.mss_load_version_tables import MSS_LoadVersionTables
from mss.m_lib.m_utils.mss_load_inserts import MSS_LoadInserts

# TODO move to scripts folder in db-autotest package
MSS_LoadInserts.insert_tables()
MSS_LoadInserts.insert_indexes()
MSS_LoadInserts.insert_columns()
inserted_id = MSS_LoadInserts.insert_version()
v_tables = MSS_LoadVersionTables(inserted_id)
v_tables().insert_into_meta_db()
v_tables().insert_columns()
v_indexes = MSS_LoadVersionIndexes(inserted_id)
v_indexes().insert_into_meta_db()
v_indexes().insert_columns()
