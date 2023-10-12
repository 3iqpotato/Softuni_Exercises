
import psycopg2  # pip install psycopg2 !


# Create connection and try. If you get some errors, then check again.
con = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='kiko369963'
)

cur = con.cursor()

query = "CREATE TABLE my_videos(id SERIAL PRIMARY KEY, date VARCHAR(30), file_path TEXT )"

cur.execute(query)
con.commit()






