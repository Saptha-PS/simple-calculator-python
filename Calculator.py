print("Hello friend,")
print("Today we are here to do some mathematical calculations.Given below are the choices you have ,it can be either addition or multiplication etc.")
print("You can enter the corresponding number to your desired choice and find out the answer.")
print("Your choices are given below:-")
print("Enter 1 for Addition.")
print("Enter 2 for Substraction.")
print("Enter 3 for Multiplication")
print("Enter 4 for Division.")
print("Enter 5 for Finding Reminder.")
print("Enter 6 for Finding Square Root of a number.")
print("Enter 7 for finding Exponents.")
print("Enter 8 for Floor Division.")
a=float(input("Enter your first number(A):")
b=float(input("Enter your second number(B):")
choice=int(input("Enter your choice:")
if choice==1:
        print("Result =",a+b)
elif choice==2:
        print("Result =",a-b)
elif choice==3:
        print("Result =",a*b)
elif choice==4:
     if b!=0:
        print("Result =",a/b)
     else:
        print("INVALID INPUT! DIVISION BY ZERO!")
elif choice==5:
        print("Result(A%B) =",a%b)
        print("Result(B%A) =",b%a)
elif choice==6:
     print("Here you can choose between your first and second numebr to find square root")
     print("For finding square root of first number enter 'F'.")
     print("For finding square root of second number enter 'S'.")
     print("For finding Square root of both numbers enter 'O'.")
     operation=input("Enter your selection:")
         if operation=="F":
                   print("Result =",a**2)
         elif operation=="S":
                   print("Result=",b**2)
         elif operation=="O":
                   print("Result=",a**2,"and",b**2)
         else:
              print("INVALID SELECTION")
elif choice==7:
        print("For finding A**B enter 'I'.")
        print("For finding B**A enter 'II'.")
        print("For finding both enter 'III'.")
        selection= input("Enter your choice:")
        if selection=="I":
                print("Result=",a**b)
        elif selection=="II":
                print("Result=",b**a)
        elif selection=="III":
               print("Result =",a**b,"and",b**a)
        else:
              print("INVALID INPUT!!")
elif choice==8:
        print("For finding A//B enter 'Y'.")
        print("For finding B//A enter 'X'."
        print("For finding both enter 'B'.")
        operation=input("Enter your choice:")
        if operation=="Y":
                 print("Result=",a//b)
        elif operation=="X":
                 print("Result=",b//a)
        elif operation=="Y":
                 print("Result=",a//b,"and",b//a)
        else:
              print("INVALID OPERATION!!")
else:
      print("INVALID OPERATION!!")
      

        
