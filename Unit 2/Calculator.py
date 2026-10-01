# Step 1: create a function that will add 2 numbers together.
 
 
# Step 2: The number should be typed by a user.

# function definition
def calculate_add(): 
    print("Program started: Please type in some numbers: ") 
    num1 = int(input())
    num2 = int(input())
    print(num1 + num2) 

# function invocation/call
calculate_add()    

def calculate_sub(): 
    print("Program started: Please type in some numbers: ")
    num1 = int(input())
    num2 = int(input())
    print(num1 - num2)
calculate_sub()


def calculate_mul(): 
    print("Program started: Please type in some numbers: ")
    num1 = int(input())
    num2 = int(input())
    print(num1 * num2)
calculate_mul()

def calculate_div(): 
    print("Program started: Please type in some numbers: ")
    num1 = int(input())
    num2 = int(input())
    print(num1 / num2)
calculate_div()

