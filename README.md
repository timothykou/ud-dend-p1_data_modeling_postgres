# Udacity Data Eng Nanodegree: Project "Data Modeling with Postgres"

## Purpose of project
Startup Sparkify wants to create a Postgres database to optimize queries on song play analysis. Currently, data is stored in JSON files and is not easily queried.

This project creates a PostgresSQL database and an ETL pipeline for adding the data from existing JSON files into the database. The database uses a star schema, and stores data in fact (songplays) and dimension (songs, artists, users, etc) tables.

Songplay (including timestamps, artists, and song information) data in the fact table is now linked to each user. For example, to see all songplays from user with user_id "30", the following query can be used:
* SELECT * FROM songplays WHERE user_id = 30;


## .py files
* sql_queries contains SQL commands for interacting with PostgresSQL database - e.g. creating/dropping tables, adding data
* create_tables.py creates database and tables.
* etl.py pulls song and log files from dir data/ and loads them into database tables

## .ipynb files
* test.ipynb confirms creation of tables with correct columns
* etl.ipynb was used for testing code in etl.py

## Schema
* See CREATE queries in sql_queries.py for full schema and data types
_Fact Table_
* songplays - records in log data associated with song plays i.e. records with page NextSong
* songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
_Dimension Tables_
* users - users in the app
    * user_id, first_name, last_name, gender, level
* songs - songs in music database
    * song_id, title, artist_id, year, duration
* artists - artists in music database saf
    * artist_id, name, location, latitude, longitude
* time - timestamps of records in songplays broken down into specific units
    * start_time, hour, day, week, month, year, weekday

