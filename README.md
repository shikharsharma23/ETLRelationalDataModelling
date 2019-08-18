## Relation Data Modelling with Postgres & ETL Pipeline for Strong streaming company
### Udacity Data Engineer Nano Degree Project 1
### Goal
This project deals with a music streaming app. The app has data in two sources. 
1. JSON logs of user activity on app
2. JSON metadata of songs in the app
To run analytics or other purposes, we require to ingest this data using ETL
This is followed by putting it into a Star schema based Fact and Dimension postgress sql relations
Once this is present, analytic queries can be quickly run over it. 

### Data base schema and design

Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimension Tables
users - users in the app
user_id, first_name, last_name, gender, level
songs - songs in music database
song_id, title, artist_id, year, duration
artists - artists in music database
artist_id, name, location, latitude, longitude
time - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday

These facts and dimensions are populated after ETL of raw json data.
This is maintained in a star schema and suitable for OLAP purposes

### Some analytic queries
1. Which is the most paid song and artist
2. Which user has paid for most songs

