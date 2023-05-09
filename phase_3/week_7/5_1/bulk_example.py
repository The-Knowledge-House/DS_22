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

# ** --> dictionary unpacking!
conn = psycopg2.connect(**params)

# with is something called a context manager : opens and closes a connection for you
with conn.cursor() as cursor:
    # (PART OF) SPRINT 6
    # DUE UNTIL 5/10 (WEDNESDAY OF NEXT WEEK)
    with open('phase_3/week_7/data/customers.csv', 'r') as f:    
        cmd = 'COPY store.customer(cust_id, fname, lname, account_create) FROM STDIN WITH (FORMAT CSV, HEADER FALSE)'
        cursor.copy_expert(cmd, f)
    conn.commit()