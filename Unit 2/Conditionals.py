# Conditional logic: these are keywords that instruct your program to do specific instructions baased on specififc data or conditions 

#conditional syntax:

grade = 89 

if grade >= 90:
    print("congrats")

else: 
    print("try again") 


    def college(): 
        grade= int(input("Please type in ya grade"))
        if grade < 90: 
            templeUApp()
        else:
            ccpApp()

def ccpApp():
    print("congrats please complete the community college app with the following code") 
    print("238293")

def TempleUApp(): 
    print("congrats please complete the temple app with the following code")
    print("a7ds78sd")

#college()                       

def calculate_add():
    print("Program started: Please type in some numbers: ") 
    num1 = int(input())
    num2 = int(input())
    print(num1 + num2) 
#calculate_add() 

def calculate_sub(): 
    print("Program started: Please type in some numbers: ")
    num1 = int(input())
    num2 = int(input())
    print(num1 - num2)
#calculate_sub()


def calculate_mul(): 
    print("Program started: Please type in some numbers: ")
    num1 = int(input())
    num2 = int(input())
    print(num1 * num2)
#calculate_mul()


def calculate_div(): 
    print("Program started: Please type in some numbers: ")
    num1 = int(input())
    num2 = int(input())
    print(num1 / num2)
#calculate_div()


#if userSelection = input(" please select an option")

if userSelection == 1:
    calculate_add()
elif userSelection == 2:
    calculate_sub()
elif userSelection == 3:
    calculate_mul()
elif userSelection == 4:
    calculate_div() 

#else:
    #print:("error. please enter a valid number.")




def movieTicket():
    print("Welcome to the theater. How old are you")
    userAge = int(input())
    if userAge <= 7:
        print( " your ticket is $8.00")
    else:
        print(" Sorry there was an error.")
    if userAge >= 8 and userAge < = 20
        print("Your ticket is $12.00")
    if userAge > = 21    
movieTicket()            

