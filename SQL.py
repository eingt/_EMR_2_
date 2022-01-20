import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'maneeshj',
    port = '3306',
    database = 'EMR'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM DOCTORS')

users = mycursor.fetchall()
print(type(users))
for user in users:
    print(user)
    print('Username ' + user[1])