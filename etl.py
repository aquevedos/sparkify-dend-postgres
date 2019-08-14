import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *



def process_song_file(cur, filepath):
    """This Function reads the json files, transform and insert the artists and their songs."""
    # open song file
    df =  pd.read_json(filepath, lines=True) 

    # insert artist record
    artist_data_col =  ['artist_id'  , 'artist_name'  , 'artist_location'  , 'artist_latitude'  , 'artist_longitude']
    artist_data = df[artist_data_col].drop_duplicates()
   
    for i, row in artist_data.iterrows():
        cur.execute(artist_table_insert, row)  
  
    
    # insert song record
    song_cols = ["song_id", "title", "year", "duration"]
    song_data = df[song_cols].drop_duplicates()
    
    for i, row in song_data.iterrows():
        cur.execute(song_table_insert, row)  

        
def process_log_file(cur, filepath):
    """This Function reads the json files, transform and insert the users, time and the fact table """
    # open log file
    df = pd.read_json(filepath, lines = True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']


    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = (t.tolist(),t.dt.hour.values.tolist(),t.dt.day.values.tolist(),
                 t.dt.week.values.tolist(),t.dt.month.values.tolist(),
                 t.dt.year.values.tolist(),t.dt.weekday.values.tolist())
    column_labels = column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    data = {column_labels[i]:time_data[i] for i in range(len(column_labels))}
    time_df = pd.DataFrame(data=data)
    
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    
    # load user table
    user_column_labels = ['userId', 'firstName', 'lastName', 'gender','level']
    user_df = df[user_column_labels].drop_duplicates()


    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)  
        

    # insert songplay records
    column_labels = ['ts', 'userId', 'sessionId', 'location','userAgent']
    songplay_df = df[column_labels].drop_duplicates()

    for index, row in songplay_df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select)
        results = cur.fetchone()
        
        cur.execute(artist_select)
        results_2 = cur.fetchone()
   
        if results:
            songid = results
            
        else:
            songid = None

        if results_2:
            artistid = results_2
            
        else:
            artistid = None
        
        
        # insert songplay record
        songplay_data = (t[index], row['userId'], songid,artistid, row['sessionId'], row['location'],row['userAgent'] )
        cur.execute(songplay_table_insert, songplay_data)   



def process_data(cur, conn, filepath, func):
    """This function reads all files in json format that are found in the data folders and will allow each file to be processed to be ingested in the corresponding table"""
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))
        
        
        

def main():
    """this function will ingest in the database sparkifydb, assuming that the tables (dimensions and table of facts) are already created"""
    
    #Connection with the Database sparkfydb in Postgres using student credencials
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    #Ingest the tables from song_data directory
    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    
    #Ingest the tables from log_data directory
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()
    
    
if __name__ == "__main__":
    main()