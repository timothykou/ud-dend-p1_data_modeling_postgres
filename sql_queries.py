# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"


# CREATE TABLES

# songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (songplay_id int, start_time timestamp, user_id int, level int, 
    song_id int, artist_id int, session_id int, location varchart, user_agent varchar)
""")

# users - users in the app
user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id int, first_name varchar, last_name varchar, gender varchar, 
    level int)
""")

# songs - songs in music database
song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id int, title varchar, artist_id int, year int, duration int)
""")


# artists - artists in music database
artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (artist_id int, name varchar, location varchar, 
    latitude numeric, longitude numeric)
""")

# time - timestamps of records in songplays broken down into specific units
time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour int, day int, week int, month int, year int, 
    weekday int)
""")


# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]