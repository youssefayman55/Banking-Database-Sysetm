# import psycopg library to connect to PostgreSQL(Supabase) database
import psycopg


# fuction to get a connection to the database
def get_db_connection():

   conn = psycopg.connect(
      'postgresql://postgres.hgaitynwoxpkmxqoiyrl:A01012837186A@aws-0-eu-west-1.pooler.supabase.com:6543/postgres'
   )
   
   return conn




