## Code for highest marks and lowest marks of a student and average



student={
  "praveen":90,
  "sai":70,
  "mani":60,
  "nani":50,
  "gopi":20,
}

highest=max(student,key=student.get)
lowest=min(student,key=student.get)

average=sum(student.values())/len(student)
for name,marks in student.items() :
  if marks>=90:
    grade="A"
  elif marks>=75:
    grade ="B"
  elif marks>=60:
    grade ="c"
    grade ="B"
  elif marks>=40:
    grade ="D"
  else :
    grade="F"
  print(name,":",marks,"-",grade)
print("Highest marks :",highest)
print("Lowest marks :",lowest)
print(average)