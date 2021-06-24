num1 = int(input("input your first number\n"))
num2 = int(input("input your second number\n"))

operations = input("""
please choose what operation you would like to choose
+
-
*
/
""")

if operations == "+":
       print(num1 + num2)
       sum1 = (num1 + num2) 
elif operations == "-":
       print(num1 - num2)
       sum2 = (num1 - num2)
elif operations =="*":
       print(num1 * num2)
       sum3 = (num1 * num2)
elif operations == "/":
       print(num1 / num2)
       sum4 = (num1 / num2)

while True:
       cont = input("would you like to continue? (y/n)")
       if cont == "y":
              num = int(input("input your other number\n"))
       
       else:
              exit()
              

       operations = input("""
       please choose what operation you would like to choose
       +
       -
       *
       /
       """)

       if operations == "+":
                     print(sum1 + num)
       elif operations == "-":
                     print(sum2 - num)
       elif operations == "*":
                     print(sum3 * num)
       elif operations == "/":
                     print(sum4 / num)
                     


