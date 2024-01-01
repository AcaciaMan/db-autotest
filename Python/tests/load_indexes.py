import db_autotest.m_lib.config.config as cn
import sqlite3

cur = cn.con.cursor()

cur.execute(
'''
SELECT t.owner, t.index_name
  FROM all_indexes t
 WHERE t.index_name IN (SELECT o.OBJECT_NAME
                          FROM obj o
                         WHERE object_type = 'INDEX'
                         and o.ORACLE_MAINTAINED = 'N' )
'''
)

#Connecting to sqlite
conn = sqlite3.connect('C:/Tools/SQLite/app/metadata.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

for x in cur:
    # print("owner", owner, index_name)

    try:
        # Preparing SQL queries to INSERT a record into the database.
        cursor.execute('''INSERT INTO M_OBJECT(
        SCHEMA, NAME, TYPE) VALUES 
        (?, ?, 'INDEX')''', x)

    except Exception:
        print("Not inserted", x)

    else:    

        # Commit your changes in the database
        conn.commit()

# Closing the connection
conn.close()
