# This gist contains a direct connection to a local PostgreSQL database
# called "suppliers" where the username and password parameters are "postgres"

# This code is adapted from the tutorial hosted below:
# http://www.postgresqltutorial.com/postgresql-python/connect/
import psycopg2

# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

# conn = psycopg2.connect("dbname=d7rdelbgg3dkvc port=5432 user=vhizlhtobmkclb password=30690f043b7f5a4974e3d2860a6435a05ba6f4fa1a4ddffa4e7e3a64454d783c")

# Or:
conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="postgres", password="POS2021@sabi")

# Create a cursor object
cur = conn.cursor()

# A sample query of all data from the "repo_land_measure" table in the "postgres" database
cur.execute("""SELECT * FROM repo_land_measure""")
query_results = cur.fetchall()
print(query_results)
# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()