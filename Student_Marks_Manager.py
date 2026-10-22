#Student Marks Manager


#STAGE-1
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
x = []

for i in students:
  a = sum(students[i])/len(students[i])
  x.append(a)
  print(f"{i} ,   {a:.2f}")


#STAGE-2
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
x = []

for i in students:
  a = sum(students[i])/len(students[i])
  x.append(a)
  if a >= 90:
    print(f"{i} ,   {a:.2f}  , A")
  elif a >= 80:
    print(f"{i} ,   {a:.2f}  , B")
  elif a >= 70:
    print(f"{i} ,   {a:.2f}  , C")


#STAGE-3
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
x = []

for i in students:
  a = sum(students[i])/len(students[i])
  x.append(a)

highest = max(x)
index = x.index(highest)

print("Highest Marks : ", highest)
print(f"Topper Name : {list(students.keys())[index]}")




#STAGE-4
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
topper=[]

while True:


  choose = int(input('''CHOOSE YOUR PROGRAM NO.:
             LIKE:- 1. ADD STUDENT,
                    2. VIEW ALL,
                    3. SHOW TOPPER,
                    4. Exit.
                                      '''))
  print("")





  if choose == 1:

    while True:
      name = input("Enter Student Name : ")

      if name in students:
        print("Student Already Exist")
        print("")
        continue

      else:
        attempts = 0
        num =[]
        while attempts < 3:
          Number = int(input("Enter Student Number : "))

          if 0< Number <=100:
            num.append(Number)
            attempts+=1
          else:
            print("INVALID INPUT")

        students[name]=num
        print("")
        print("ADD SUCCESSFULLY")
        print("")
        break



  elif choose == 2:
    print(students)
    print("")




  elif choose == 3:

    for i in students:
      a = students[i]
      a = sum(a)/len(a)
      topper.append(a)
    highest = max(topper)
    b = topper.index(highest)
    print("TOPPER  : " , list(students.keys())[b])
    print("")


  elif choose == 4:
    print("❤️ GOODEBYE ! 😉")
    print("")
    break


  else:
    print("WRONG SELECTION PLEASE SELECT THE AVAILABLE OPTION")
    print("")






