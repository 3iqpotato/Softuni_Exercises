import pathlib

import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='kiko369963'
)

cur = con.cursor()

files = pathlib.Path('C:/Users/KIKO-ASUS/Videos')
filtered_data = list(files.rglob('*.mkv'))



for f in filtered_data:
    date = f.parts[4].split(' - ')
    file_path = str(f)

    query = '''INSERT INTO my_videos(date, file_path)
    VALUES
        (%s, %s)
    '''

    cur.execute(query, (date, file_path))

con.commit()

for row in data:
    print(row)
obj_list = []
for row in data:
    for col in row:
        print(col)
    obj_list.append(Song(row[2], row[1], row[3]))

con.close()