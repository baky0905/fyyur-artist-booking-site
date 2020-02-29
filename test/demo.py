import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="Kikirobi1")

cursor = conn.cursor()

# cursor.execute(
#     """
#     CREATE TABLE table2(
#         id INTEGER PRIMARY KEY,
#         completed BOOLEAN NOT NULL DEFAULT False
#     );
#     """
# )

test = [(6, False), (7, True)]


for t in test:
    cursor.execute("INSERT INTO table2(id, completed) VALUES(%s, %s);", t)

conn.commit()

conn.close()


conn = psycopg2.connect(database="postgres", user="postgres", password="Kikirobi1")

cursor = conn.cursor()

cursor.execute("SELECT * FROM table2;")

result = cursor.fetchall()
print(result)

