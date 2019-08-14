import psycopg2
from sql_queries import create_table_queries, drop_table_queries , alter_table_queries



def create_database():
    """This function creates the connection with the student of the database (database created in the previous examples of practice), removes it and creates the database sparkifydb"""
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """ This function that allows to eliminate the tables from the sparkifydb database as long as they exist."""
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

        
def create_tables(cur, conn):
    """This function that allows creating the tables in the sparkifydb database if there are no"""
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

        
def alter_table(cur, conn):
    """This function that alters the table to create the foreign keys  """
    for query in alter_table_queries:
        cur.execute(query)
        conn.commit()
        
    
def main():
    """Main function that calls the other functions declared (function of creating the database, function of elimination of the tables if they exist,
    function to create the tables and alter them, to create their foreign keys."""
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)
    alter_table(cur, conn)
    conn.close()


if __name__ == "__main__":
    main()