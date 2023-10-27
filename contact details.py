contact={}
while True:
    ch=int(input("enter choice:\n1.add contact\t2.show contact\n3.exit"))
    match ch:
        case 1:
            print("\n add.contact")
            m=input("enter mobile number:")
            n=input("enter name:")
            contacts[m]=n
            print("contact added")
        case 2:
            print("\n show contact")
            print("\n mo no","name")
            for k ,v in contact.items():
                print(k,v)
        case 3:
            print("\n exiting")
            break
        case_:
            print("\n INVALID INPUT")
