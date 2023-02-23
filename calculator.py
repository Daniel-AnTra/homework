class calculator:
    def addition(self):
        return (x + y)
    def substraction(self):
        return (x - y)
    def multiplication(self):       
        return (x * y)
    def division(self):
        return (x / y) 

obj1 = calculator()
choice = 1
while choice != 0:
        x = int(input("Enter the first number: ")) 
        y = int(input("Enter the second number: "))
        print ("1. Addition")
        print ("2. Substraction")
        print ("3. Multiplication")
        print ("4. Division")
        choice = int(input("Enter your choice of operation : "))
        if choice == 1:
            print("The result is " + str(obj1.addition()))
            yesno = str(input("Do you want new caluclation : press y/n "))
        elif choice == 2:
            print("The result is " + str(obj1.substraction()))
            yesno = str(input("Do you want new caluclation : press y/n "))
        elif choice == 3:
            print("The result is " + str(obj1.multiplication()))
            yesno = str(input("Do you want new caluclation : press y/n "))
        elif choice == 4:
            print("The result is " + str(obj1.division()))   
            yesno = str(input("Do you want new caluclation : press y/n "))  
        else:
            print("Invalid choice. Choose one of the operations on the list")
            yesno = str(input("Do you want new caluclation : press y/n "))  
            
        if  yesno == "y":
            while choice != 0:
                x = int(input("Enter the first number: ")) 
                y = int(input("Enter the second number: "))
                print ("1. Addition")
                print ("2. Substraction")
                print ("3. Multiplication")
                print ("4. Division")
                choice = int(input("Enter your choice of operation : "))
                if choice == 1:
                    print("The result is " + str(obj1.addition()))
                elif choice == 2:
                    print("The result is " + str(obj1.substraction()))
                elif choice == 3:
                    print("The result is " + str(obj1.multiplication()))
                elif choice == 4:
                    print("The result is " + str(obj1.division()))     
                else:
                    print("Invalid choice. Choose one of the operations on the list")
        elif yesno == "n":
            break