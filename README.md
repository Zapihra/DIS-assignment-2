# DIS-assignment-2
Univeristy work for data intensive systems

## Initial
- Use venv for virtual environment
- Change the postgresql password and user on postgresConnect.py line 5
- No initial database is created in the code itself

### Dependencies
- psycopg2
- pymongo

### Database structure

- MongoDB, data in DIS.Dogs.json
Database name: DIS
Subdatabase name: Dogs
Columns: name, breed, age

- Postgresql, data in owner.csv and cat.csv
Database name: owner
Table name: owners
Columns: name, email

Database name: cat
Table name: cats
Columns: name, breed, age

