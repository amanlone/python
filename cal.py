num1 = int(input("input your first number"))
num2 = int(input("input your second number"))

operations = input("""
please choose what operation you would like to choose
+
-
*
/
""")

if operations == "+":
    print(num1 + num2)
elif operations == "-":
    print(num1 - num2)
elif operations =="*":
    print(num1 * num2)
elif operations == "/":
    print(num1 / num2)
