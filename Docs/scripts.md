# Useful scripts

## Create SQLite schema backup sql

```cmd

sqlite3 C:\work\GitHub\db-autotest\Docs\m_sqlite.db
sqlite3 C:/work/m_mssql.db

.output ./backup_schema.sql
.schema
.exit

.read ./backup_schema.sql
.exit
```

## Upload Test.pypi.org package

```cmd

py -m pip install --upgrade build

py -m build

py -m pip install --upgrade twine

py -m twine upload --repository testpypi --config-file .pypirc dist/*

py -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE

```
