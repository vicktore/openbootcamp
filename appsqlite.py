import  sqlite3

db_connection = sqlite3.connect("my-app.sqlite")
db_cursor = db_connection.cursor()

db_cursor.execute("create table students(id,"name","lastname")")

db_cursor.execute("indice (id)")

db_cursor.execute("insert into students values (1, 'estudiante1', 'clave1')")
db_cursor.execute("insert into students values (2, 'estudiante2', 'clave2')")
db_cursor.execute("insert into students values (3, 'estudiante3', 'clave3')")
db_cursor.execute("insert into students values (4, 'estudiante4', 'clave4')")
db_cursor.execute("insert into students values (5, 'estudiante5', 'clave5')")




db_connection.commit()

db_cursor.execute("select * from students where name = 'estudiante1'")

row = db_cursor.fetchall()
print(row)

db_connection.close()
