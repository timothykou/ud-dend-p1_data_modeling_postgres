# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"


# CREATE TABLES

# songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    start_time timestamp NOT NULL, 
    user_id int NOT NULL, 
    level varchar, 
    song_id varchar, 
    artist_id varchar, 
    session_id int NOT NULL, 
    location varchar, 
    user_agent varchar)
""")

# users - users in the app
user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id int PRIMARY KEY, 
    first_name varchar, last_name varchar, gender varchar, 
    level varchar NOT NULL )
""")

# songs - songs in music database
song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id varchar PRIMARY KEY, 
    title varchar NOT NULL, 
    artist_id varchar NOT NULL, 
    year int, 
    duration int)
""")


# artists - artists in music database
artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar PRIMARY KEY, 
    name varchar NOT NULL, 
    location varchar, latitude numeric, longitude numeric)
""")

# time - timestamps of records in songplays broken down into specific units
time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time timestamp PRIMARY KEY, 
    hour int, day int, week int, month int, year int, weekday int)
""")


# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) \
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET 
    level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration ) \
VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude ) \
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday ) \
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id
FROM songs AS s
WHERE s.title = (%s)
""")
 #, a.artist_id
# INNER JOIN artists AS a ON s.artist_id = a.artist_id
#  AND
#     a.name = %s AND
#     s.duration = %s


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]