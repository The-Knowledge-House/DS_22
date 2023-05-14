import psycopg2
import psycopg2.extras

params = {
    "host"      : "rds-pg-jobs.chfavwsr5bmp.us-east-1.rds.amazonaws.com",
    "dbname"    : "postgres",
    "user"      : "postgres",
    "password"  : "...",
    "port" : "5432"     
}

# ** --> dictionary unpacking!
conn = psycopg2.connect(**params)

# with is something called a context manager : opens and closes a connection for you
with conn.cursor() as cursor:
    with open('phase_3/week_8/5_8/function_ex.sql', 'r') as functions:
        queries = functions.read()
        cursor.execute(queries)

    try:
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
