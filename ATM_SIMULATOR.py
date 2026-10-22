
#ATM SIMULATOR


balance =10000
pin = '1234'
attempts = 3
history=[0,0]

while attempts>0:
  user_pin= input("Enter Your PIN  : ")
  print()

  if user_pin == pin :

    while True:
      a = int(input('''ENTER YOUR PROGRAM NO.:
             LIKE:- 1. BALANCE,
                    2. DEPOSITE,
                    3. WIHDRAWL,
                    4. Exit.
                                      '''))
      print("")

      if a == 1 :
        print("BALANCE RIGHT NOW : ", balance)
        print()



      elif a == 2 :
        x=int(input("ENTER DEPOSITE AMOUNT : "))
        print()
        if x>0:
          balance = balance + x
          history[0]=x
          print("Deposite Amount : ", x)
          print("BALANCE RIGHT NOW : ", balance)
          print()
        else:
          print("INVALID AMOUNT")
          print()


      elif a == 3 :
        y=int(input("ENTER WITHDRAWL AMOUNT : "))
        print()
        if y>0 and y<=balance:
          balance = balance - y
          history[1]=y
          print("Withdral Amount : ", y)
          print("BALANCE RIGHT NOW : ", balance)
          print()
        else:
          print("INVALID AMOUNT")
          print()


      elif a == 4 :
        print("Exit")
        print("DEPOSITE AMOUNT : ", history[0])
        print("WITHDRAWL AMOUNT : ", history[1])
        print()
        attempts=0
        break

      else:
        print("No Such Program No. Exist {Invalid Input}")
        print("")
        print()


  else:                          #this doing ki attempts count kar rha hai or ye 1 while vale loop ke under hai
    attempts = attempts - 1
    print("WRONG PIN")
    print("Attempts Left : ",attempts)
    print()
    if attempts == 0:
      print("CARD BLOCKED")




