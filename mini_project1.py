## Simple notes app
## This code allows the user to add notes,view saved notes

while True:
  print("\nTo add a new note enter 1")
  print("To view the note enter 2")
  print("To exit enter 3")
  choice=int(input("Enter choose: "))

  if choice==1:
    file=open("text.txt","w")
    file.write(input("Enter note: "))
    print("Note entered")
  
  
  elif choice==2:
    file=open("text.txt","r")
    print(file.read())
    
  
  elif choice==3:
    print("Bye")
    break

  else:
    print("invalid choice")
