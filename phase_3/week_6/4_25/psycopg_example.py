import psycopg2
import psycopg2.extras
import csv
import os

# aws rds 
"""
params = {
    "host"      : "rds-pg-jobs.chfavwsr5bmp.us-east-1.rds.amazonaws.com",
    "dbname"    : "postgres",
    "user"      : "postgres",
    "password"  : "secret",
    "port" : "5432"     
}
"""

params = {
    "host"      : "localhost",
    "dbname"    : "postgres",
    "user"      : "postgres",
    "password"  : "password",
    "port" : "5434"     
}

# SPRINT 5
# NOT DUE UNTIL 5/3 (WEDNESDAY OF NEXT WEEK)
# ** --> dictionary unpacking!
conn = psycopg2.connect(**params)

# with is something called a context manager : opens and closes a connection for you
with conn.cursor() as cursor:
    # READ FILES IN PYTHON
    with open('phase_3/week_6/4_25/schema.sql', 'r') as schema:
        # read --> reads in entire file
        queries = schema.read()
        print(queries)
        # we are starting a transaction (or continuing)
        cursor.execute(queries)
    # commit your changes
    conn.commit()