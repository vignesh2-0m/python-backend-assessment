import psycopg2

conn = psycopg2.connect(
    dbname="repo_dp",
    user="postgres",
    password="vignesh123",
    host="localhost",
    port="5432"
)

print("Connection successful!")
conn.close()