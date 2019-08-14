# Data Modeling with Postgres: Song Play Analysis using PostgreSQL and python
> Anita Quevedo Solidoro

This ETL Pipeline was designed for a startup **Sparkify**, who wants to analyze their information collected about the songs and the activity of their users in their new music streaming application, 

### Files in Project
The files for running the project are:

* `create_tables.py`: Script drop tables if exist, to create and modify relations that between.

* `sql_queries.py`: Script with the queries and scripts to use in create_tables.py and etl.py.

* `etl.py`: Script that automatically browse the directories and read each json file, using pandas and inserting the tables defined in the previous script.


* `prueba2.ipynb`:  Notebook with the step by step of the process , the content is equals to etl.py. 

* `test.ipynb`: Notebook that test that the tables are created and fill with the data from the etl process.


### Objectives:

**For the solution a dimensional model was proposed (composed of a table of facts and 4 dimensions) with the purpose of:**

- Help the startup called Sparkify to analyze their information collected about the songs and the activity of their users in their new music streaming application, the same one that resides in a directory of json records, the queries are not complicated, since these only involve the table of facts and dimensions.

- To be able to calculate indicators to measure the behavior of the client in front of listening to their music, being able to analyze their past and allowing to apply data mining techniques to be able to do analytical and allow to make better decisions in the future, thus improving the possible business that they would like to do


## Justification of ETL design and pipeline:

- A star model was planted, see attached image:
	https://screenshot.net/x7r31u4

Explication: 
####  -  Fact table
* `songplays`: records in log data associated with song plays i.e. records with page NextSong
*songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent*

	
#### -  Dimension Tables
* `users`: users in the app
*user_id, first_name, last_name, gender, level*

* `songs`: songs in music database
*song_id, title, artist_id, year, duration*

* `artists`: artists in music database
*artist_id, name, location, lattitude, longitude*

* `time`: timestamps of records in songplays broken down into specific units
*start_time, hour, day, week, month, year, weekday*


In the ETL pipeline, the dimensions were first created, and then the facts table was created, then to populate them the dimensions are ingested and then the fact table. You have to follow that order since the fact table has foreign keys.
(When creating the songsplays facts table, I had to use the alter table command to add the foreign keys)


## Steps to follow for Pipiline:
https://screenshot.net/q5dnobg
Run  : 
 - 1° : pyhton  create_tables.py
 - 2°:  pyhton etl.py
 - 3° Open jupyter and test.ipynb: to verify if the tables and their registers  exist.


## Analysis query:
https://screenshot.net/4kzyxs9

It shows the clients with their respective user_id, full name (first_name and last_name) and their current level, that is, whether it is paid or free.




