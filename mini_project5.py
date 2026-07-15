## This code helps to store the expenses,add sum of expenses

expenses={}
while True:
  print("\n1.Add EXpenses"
        "\n2.View Expenses"
        "\n3.Show Total Expenses"
        "\n4.Exit")
  print("Please Enter only the numbers")
  
  choice=int(input("Ether your choice: "))

  if choice==1:
    add=input("Enter Expenses: ")
    add1=int(input("Enter Amount: "))
    expenses[add]=add1
    print("Added sucessfuly..")

  elif choice==2:
    print("\n",expenses)

  elif choice==3:
    print("\nTotal expenses")
    print(sum(expenses.values()))

  elif choice==4:
    print("\nExiting...")
    break

  else:
    print("\nPlease enter a correct option..!")

  

