## library notes app used for Add,Borrow,Return the books 


library={}
while True:
  print("\n1.Add Book"
        "\n2.Borrow Book"
        "\n3.Return Book"
        "\n4.View Book"
        "\n5.Exit")
  choice=int(input("\nEnter your choice: "))
  if choice==1:
    book=(input("\nEnter new book: "))
    
    if book in library:
      print("Book is already exists..")
    else:
      library[book]="Available"
      print("sucessfuly add book")
  
  elif choice==2:
    book=input("\nenter book name to borrow: ")
    if book in library:
      if library[book]=="Available":
        library[book]="Borrow"
        print("Book borrow sucesfuly ")
      else:
        print("Book already borrow")

    else:
      print("Book not found")
  
  elif choice==3:
    book=input("\nEnter return book name: ")
    if book in library:
      if library[book]=="Borrow":
        library[book]="Avalable"
        print("Book return sucessfuly")
      else:
        print("enter a book you borrow")
    else:
      print("please enter a correct book")

  elif choice==4:
    print(library)
  
  elif choice==5:
    print("thank you for visit. Bye")
    break
  else:
    print("invalid choice")

