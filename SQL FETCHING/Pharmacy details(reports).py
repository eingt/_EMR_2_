import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='maneeshj',
    port='3306',
    database='EMR'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM PHARMACY')

Pharmacy_details = mycursor.fetchall()

for Pharmacy in Pharmacy_details:
    print(patients)
    print('Medicine id' + Pharmacy[0])
    print('Manufacture company' + Pharmacy[1])
    print('Stock' + Pharmacy[2])
    print()