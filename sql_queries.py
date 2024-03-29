# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop =  "DROP TABLE IF EXISTS users"
song_table_drop =  "DROP TABLE IF EXISTS songs"
artist_table_drop =  "DROP TABLE IF EXISTS artists"
time_table_drop =  "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
(songplay_id  serial PRIMARY KEY, start_time TIME, user_id integer, level text, song_id text, artist_id text, session_id integer,
location text, user_agent text)""") 

user_table_create = ("""CREATE TABLE IF NOT EXISTS users
(user_id integer PRIMARY KEY, first_name text,last_name text, gender text, level text)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs
(song_id text, title text,artist_id text, year integer, duration float)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists
(artist_id text, name text, location text, latitude text, longitude text)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time
(start_time TIME, hour integer, day integer, week integer, month integer, year integer, weekday integer)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time , user_id , level , song_id , artist_id , session_id ,location , user_agent ) VALUES 
(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""INSERT INTO users (user_id , first_name ,last_name , gender , level ) VALUES 
(%s,%s,%s,%s,%s) ON CONFLICT(user_id) DO UPDATE
    SET first_name = excluded.first_name,
        last_name = excluded.last_name,
        gender = excluded.gender,
        level = excluded.level;
""")

song_table_insert = ("""INSERT INTO songs (song_id , title ,artist_id , year , duration) VALUES 
(%s,%s,%s,%s,%s)
""")

artist_table_insert = ("""INSERT INTO artists (artist_id , name , location , latitude , longitude ) VALUES 
(%s,%s,%s,%s,%s)
""")


time_table_insert = ("""INSERT INTO time (start_time , hour , day , week , month , year , weekday ) VALUES 
(%s,%s,%s,%s,%s,%s,%s)
""")

# FIND SONGS
song_select = ("""Select songs.song_id, artists.artist_id from songs   JOIN artists ON songs.artist_id = artists.artist_id WHERE 
songs.title = %s AND artists.name = %s AND songs.duration = %s 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]