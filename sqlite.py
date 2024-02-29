from sqlite3 import *
from sqlite3 import Error

def create_connection(path:str):
    connection = None

    try:
        connection=connect(path)
        print("link")
    except Error as e:
        print(f"Error:{e}")

    return connection;

def Execute_Query(connection,query:str):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("tabel koik")
    except Error as e:
        print(f"tea:{e}")

def Execute_Query_Read(connection, query:str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result= cursor.fetchall()
        return result
    except Error as e:
        print(f"vaga:{e}")

def Execute_Query_Delete(connection, query:str):

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("\ndel tb/db\n")
    except Error as e:
        print(f"del:{e}")

### SQL ###
cr_user_tb="""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    student BOOLEAN
);
"""
cr_user = """
   insert into users(name,age,gender,student)
   values ('alex',20,'m',true),
          ('fred',23,'m',false),
          ('david',20,'?',false),
          ('alex',20,'m',true),
          ('god?',1999,'?',false);

"""
select_user = "select * from users;"

del_user_data="""
    delete from users where student = true;
"""

del_user_tb="drop table users;"


### user ###
conn = create_connection("./data.db")
Execute_Query(conn,cr_user_tb)
Execute_Query(conn,cr_user)
users = Execute_Query_Read(conn,select_user)
print("user")
for user in users:
    print(user)

Execute_Query_Delete(conn,del_user_data)

users = Execute_Query_Read(conn,select_user)
print("user")
for user in users:
    print(user)

Execute_Query_Delete(conn,del_user_tb)
Execute_Query_Delete(conn,del_user_tb)