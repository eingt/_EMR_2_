name = input("Enter name of the doctor: ")
age = input("Enter age of the doctor: ")
gender = input("Enter gender of the doctor: ")
doctor_id = input("Enter ID of the doctor: ")
department = input("Enter department of the doctor: ")
phone_number = input("Enter phone number of the doctor: ")
email = input("Enter email of the doctor: ")
address = input("Enter address of the doctor: ")
joining_date = input("Enter joining date of the doctor: ")
salary = input("Enter salary of the doctor: ")

file = open("DoctorDetails.txt", "w")
file.write(name)
file.write("\n")
file.write(age)
file.write("\n")
file.write(gender)
file.write("\n")
file.write(doctor_id)
file.write("\n")
file.write(department)
file.write("\n")
file.write(phone_number)
file.write("\n")
file.write(email)
file.write("\n")
file.write(address)
file.write("\n")
file.write(joining_date)
file.write("\n")
file.write(salary)
file.write("\n")
file.close()
#commentdghsg