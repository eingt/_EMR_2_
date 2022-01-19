def main():
    f = open('asx.txt','w')
    Patient_name = input("Enter patient name")
    Doctor_name = input("Enter the doctor name")
    Doctor_Dep = input("Enter the doctors department")
    Date = input("Enter the date")
    Time = input("Enter the time")

    f.write(Patient_name)
    f.write(Doctor_name)
    f.write(Doctor_Dep)
    f.write(Date)
    f.write(Time)

    f.close()