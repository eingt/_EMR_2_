dateTime = input("Enter date & time: ")
allpatientdetails = input("Enter All Patient Details: ")
docnameAndDep = input("Enter Doctor Name & Department: ")
prob = input("Enter What the problem is: ")
bill = input("Enter Consultation Bill (Amt Paid): ")
med = input("Enter the Medicines Prescribed: ")

file = open("patientCaseDetails.txt", "w")
file.write(dateTime)
file.write("\n")
file.write(allpatientdetails)
file.write("\n")
file.write(docnameAndDep)
file.write("\n")
file.write(prob)
file.write("\n")
file.write(bill)
file.write("\n")
file.write(med)
file.close()
