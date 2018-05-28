# python-db-migration
A docker based approach to execute db migrations.

### Problem Statement

A database upgrade requires the execution of numbered scripts stored in a specified folder, e.g. SQL scripts such as 045.createtable.sql.

- There may be gaps in the numbering and there isn't always a . (dot) after the number. 

- The database upgrade is based on looking up the current version in the database and comparing this number to the numbers in the script names. 

- If the version number from the db matches the highest number from the script then nothing is executed. 

- If the number from the db is lower than the highest number from the scripts, then all scripts that contain a higher number than the db will be executed against the database. 

- In addition, the database version table is updated after the install with the highest number. 

### Usage
```
cd scripts
python migrations.py [DBUSER] [DBHOST [DBNAME] [DBPASS]
```

### Some points to consider
- Use **docker-compose up -d** command to setup the database and to pre-load the necessary db schema.
- **create-db-schema.sh** should fire up when the shell image is up & running. This script will setup the **versionsTable** in the database. If it doesn't fire up, please execute this script manually inside the shell container.
- Please change the database credentials in **docker-compose.yaml** file if you need to.
- There is no need to use docker based approach, you can still use the migration script as mentioned in **Usage** section if you have the database credentials & versionsTable ready.
- The migrations will only work with MySQL service.
- Some sample sql scripts have been provided in the scripts directory. Please feel free to modify or remove them.
- This is not the best solution and it has much room for the improvement. I am keen to listen your feedback.

