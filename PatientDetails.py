name = input("Enter name of the patient: ")
age = input("Enter age of the patient: ")
gender = input("Enter gender of the patient: ")
patient_id = input("Enter ID of the patient: ")
department = input("Enter department of the patient: ")
phone_number = input("Enter phone number of the patient: ")
email = input("Enter email of the patient: ")
address = input("Enter address of the patient: ")
joining_date = input("Enter joining date of the patient: ")
salary = input("Enter salary of the patient: ")

file = open("patientDetails.txt", "w")
file.write(name)
file.write("\n")
file.write(age)
file.write("\n")
file.write(gender)
file.write("\n")
file.write(patient_id)
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
