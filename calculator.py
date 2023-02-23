class calculator:
    def addition(self):
        return(x + y)
    def substraction(self):
        return (x - y)
    def multiplication(self):       
        return (x * y)
    def division(self):
        return (x / y) 
x = int(input("Enter the first number: ")) 
y = int(input("Enter the second number: "))
obj1 = calculator()
choice = 1
while choice != 0:
        print ("1. Addition")
        print ("2. Substraction")
        print ("3. Multiplication")
        print ("4. Division")
        choice = int(input("Enter you choice of operation : "))
        if choice == 1:
            print("The result is " + str(obj1.addition()))
            break
        elif choice == 2:
            print("The result is " + str(obj1.substraction()))
            break
        elif choice == 3:
            print("The result is " + str(obj1.multiplication()))
            break 
        elif choice == 4:
            print("The result is " + str(obj1.division())) 
            break     
        else:
            print("Invalid choice. Choose one of the operations on the list")