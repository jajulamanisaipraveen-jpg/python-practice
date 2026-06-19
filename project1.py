## Find the largest number,shortest number ,sem of the numbers in a list

numbers = list(map(int,input("Enter any 5 numbers: ").split()))

numbers.sort()
sum =0
for i in numbers:
  sum = sum+i

print("largest number:  ",numbers[-1],"\nsmallest number: ",numbers[0])
print("sum of the list: ",sum)