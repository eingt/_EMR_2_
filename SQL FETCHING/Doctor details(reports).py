import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'maneeshj',
    port = '3306',
    database = 'EMR'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM DOCTOR')

docotors = mycursor.fetchall()

for doctor in doctors:
    print(doctors)
    print('Doctor id' + doctor[0])
    print('Doctor name'+ doctor[1])
    print('Gender'+ doctor[2])
    print('Doctor department'+ doctor[3])
    print('Joining date' + doctor[4])

    print()
