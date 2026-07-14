## Code for save,search and view contacts

contact={}
while True:
  print("\n1.Add contact",
        "\n2.Search contact",
        "\n3.View all contacts",
        "\n4.Exit\n")
  choice=int(input("Enter your choice :"))

  if choice==1:
    name=input("Enter name of the contact: ")
    phn=input("Enter phone number: ")
    contact[name]=phn
    print("Contact saved..")

  elif choice==2:
    name=input("Enter name: ")
    if name in contact:
      print("Phone number: ",contact[name])
    else:
      print("contact not found")

  elif choice==3:
    if contact:
      print("\n All contact")
      for name,phn in contact.items():
        print(name,":",phn)
    else:
      print("List is empty")

  elif choice==4:
    print("Exiting..")
    break
  
