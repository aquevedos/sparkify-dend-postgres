# DROP TABLES

user_table_drop = " DROP TABLE IF  EXISTS users "
song_table_drop = " DROP TABLE IF  EXISTS songs "
artist_table_drop = "DROP TABLE IF  EXISTS artists "
time_table_drop = "DROP TABLE IF  EXISTS tiempo "
songplay_table_drop = "DROP TABLE IF  EXISTS songplays "



# CREATE TABLES


user_table_create = ("""CREATE TABLE IF NOT EXISTS users ( user_id int PRIMARY KEY , 
first_name varchar NOT NULL, 
last_name varchar NOT NULL, 
gender char NOT NULL, 
level varchar NOT NULL);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs  ( song_id varchar PRIMARY KEY, 
title varchar NOT NULL, 
year int NOT NULL, 
duration float NOT NULL );
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists  ( artist_id varchar  PRIMARY KEY, 
name varchar NOT NULL, 
location varchar NOT NULL, 
latitude float , 
longitude float);
""")


time_table_create = ("""CREATE TABLE IF NOT EXISTS tiempo   ( start_time timestamp PRIMARY KEY,
    hour int NOT NULL,
     day int NOT NULL, 
     week int NOT NULL, 
     month int NOT NULL,
      year int NOT NULL, 
      weekday int NOT NULL ); 
""")


songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songsplays ( songplay_id serial , 
start_time timestamp NOT NULL,  
user_id int  NOT NULL, 
song_id varchar  NOT NULL,  
artist_id varchar NOT NULL, 
session_id int , 
location text  , 
user_agent text  ,
PRIMARY KEY (songplay_id )
); """)


#ALTER FACT TABLE

songplay_table_alter = (""" ALTER TABLE songsplays ADD CONSTRAINT constraint_artist_id FOREIGN KEY (artist_id) REFERENCES artists (artist_id);
ALTER TABLE songsplays ADD CONSTRAINT constraint_user_id FOREIGN KEY (user_id) REFERENCES users (user_id);
ALTER TABLE songsplays ADD CONSTRAINT constraint_song_id FOREIGN KEY (song_id) REFERENCES songs (song_id);
ALTER TABLE songsplays ADD CONSTRAINT constraint_start_time FOREIGN KEY (start_time) REFERENCES tiempo (start_time);
""" )




# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songsplays (start_time, user_id, song_id, artist_id, session_id, location, user_agent )  VALUES (%s, %s, %s, %s, %s, %s, %s) ;
""")


user_table_insert = (""" INSERT INTO users (user_id , first_name  , last_name  , gender , level )  VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) 
DO UPDATE
       SET level = EXCLUDED.level
           """)


song_table_insert = ("""INSERT INTO songs (song_id, title, year, duration) VALUES (%s, %s, %s, %s) ON CONFLICT (song_id) 
DO NOTHING;
""")


artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) 
DO NOTHING;
 """)

          
time_table_insert = ("""INSERT INTO tiempo (start_time, hour, day, week, month, year, weekday ) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) 
DO NOTHING;
""")



# FIND SONGS

song_select = (""" select s.song_id from songs s   """)
artist_select = (""" select a.artist_id from artists a   """)

#where                 s.title= (%s) and a.name = (%s) and s.duration = (%s)
# QUERY LISTS

create_table_queries = [ user_table_create, artist_table_create, song_table_create,  time_table_create, songplay_table_create]
drop_table_queries = [ user_table_drop, artist_table_drop,song_table_drop,  time_table_create, songplay_table_create]
alter_table_queries = [songplay_table_alter]
