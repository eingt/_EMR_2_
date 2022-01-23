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

patients = mycursor.fetchall()

for patient in patients:
    print(patients)
    print('Patient id' + patient[0])
    print('Patient name'+ patient[1])
    print('Date of birth'+ patient[2])
    print('Registration date'+ patient[3])

    print()
