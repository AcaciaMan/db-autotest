import pyodbc

conn_str = (
    r'Driver=ODBC Driver 18 for SQL Server;'
    r'Server=localhost;'
    r'Database=m_company;'
    r'Trusted_Connection=yes;'
    r'TrustServerCertificate=yes;'
)

conn = pyodbc.connect(conn_str) 


SQL_QUERY = """
select table_schema, table_name 
  from information_schema.tables
  where 1=1
  and TABLE_TYPE = 'BASE TABLE'    
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r.table_schema}\t{r.table_name}")

