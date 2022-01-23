import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='maneeshj',
    port='3306',
    database='EMR'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM BILING')

Billings = mycursor.fetchall()

for Billing in Billings:
    print(patients)
    print('Medicine ID' + Billing[0])
    print('Patient name' + Billing[1])
    print('Prescribed by' + Billing[2])
    print('Date' + Billing[3])
    print()