import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='maneeshj',
    port='3306',
    database='EMR'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM APPOINMENTS AND SCHEDULING')

Appointments_scheduling = mycursor.fetchall()

for Appoinment_and_scheduling in Appointments_scheduling:
    print(patients)
    print('Patient name' + Appoinment_and_scheduling[0])
    print('Doctor name' + Appoinment_and_scheduling[1])
    print('Date' + Appoinment_and_scheduling[2])
    print('Time' + Appoinment_and_scheduling[3])
    print()