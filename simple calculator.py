def add(a, b):
    answer = a + b
    print(str(a) + "+" + str( b)+ "=" + str(answer) + "\n")
def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b )+ "=" + str(answer) + "\n")
def multiply(a, b):
    answer = a * b
    print(str(a) + "*" + str(b)+ "=" + str(answer) + "\n")
def divide(a, b):
    answer = a / b
    print(str(a) + "/" + str(b)+ "=" + str(answer)+ "\n")

while True:
    print("A.Addition")
    print("B.SUBTRACTION")
    print("C.MULTIPLY")
    print("D.DIVION")
    print("E.exit")

    choice = input("input your choice : ") 

    if choice == "a" or  choice == "A":
        print("Addition")
        a = int(input("Enter your first number :" ))
        b = int(input("Enter your second number : "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Enter your first number : "))
        b = int(input("Enter your second number : "))
        sub(a, b)
    elif choice =="c" or choice == "C":
        print("Multiply")
        a = int(input("Enter ypur first number : "))
        b = int(input("Enter your second number : "))
        multiply(a, b)
    elif choice =="d" or choice == "D":
        print("Divide")
        a = int(input("Enter ypur first number : "))
        b = int(input("Enter your second number : "))
        divide(a, b)   
    elif choice =="e" or choice == "E":
        print("Program ended")
        quit()

