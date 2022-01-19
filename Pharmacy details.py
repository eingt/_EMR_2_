def appoinments():

    Medicine_name = input("Enter medicine name")
    Manufacture_Company = input("Enter the manufacturing company")
    Stock = input("Enter the stock")
    Medicine_id = input("Enter the medicine id")
    Price = input("Enter the price")
    f = open('phm.txt', 'w')

    f.write(Medicine_name)
    f.write(Manufacture_Company)
    f.write(Stock)
    f.write(Medicine_id)
    f.write(Price)

    f.close()
appoinments()