# MSSQLSERVER scripts

```cmd
net start MSSQLSERVER

net start SQLSERVERAGENT

net start SQLBrowser

```

```cmd

net stop SQLBrowser

net stop SQLSERVERAGENT

net stop MSSQLSERVER

```

```sql

select * 
  from information_schema.tables
  where 1=1
  and TABLE_TYPE = 'BASE TABLE';

  

```
