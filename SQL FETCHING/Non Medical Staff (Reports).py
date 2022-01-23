import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='maneeshj',
    port='3306',
    database='EMR'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM NON MEDICAL STAFF')

Non_medical_staff = mycursor.fetchall()

for Non_medical in Non_medical_staff:
    print(patients)
    print('Staff id' + Non_medical[0])
    print('Name' + Non_medical[1])
    print('Gender' + Non_medical[2])
    print('Department' + Non_medical[3])
    print('Joining date' + Non_medical[4])

    print()



























