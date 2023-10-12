import psycopg2  # pip install psycopg2 !

# Create connection and try. If you get some errors, then check again.
con = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='kiko369963'
)
# Create cursor object. Cursor is a object that loop over rows in db when select or insert multiple rows.
cur = con.cursor()

# Create query
query = 'SELECT * FROM MOCK_DATA '

# Execute query from cursor.
cur.execute(query)

# You can create insert query and execute in the same way

# "Explode" data from cursor into data structure if we expect some data to be returned into the cursor.
#  For example if we execute insert query, then no data will be returned.
data = cur.fetchall()

# Loop over the data
for row in data:
    print(row)

# Create insert quety
# query = '''INSERT INTO music(song_name, style, path)
# VALUES
#     ('For whom the bell tolls', 'metal', 'C:/music'),
#     ('Billie Jean', 'pop', 'C:/music'),
#     ('My Way', 'swing', 'C:/music')
# '''
#
# cur.execute(query)
# # When you manipulate the data don't forget to commit (save) changes!
# con.commit()
# con.close()