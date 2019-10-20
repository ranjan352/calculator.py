# A simple calculator

# commaSeperated
# spaceSeperated

# newLine : loop
def get_input():
    numbers = []
    numbers_string = input("Enter comma separated integer value : ")
    for num in numbers_string.split(','):
        try:  # use for value error
            numbers.append(int(num))
            print('asdf')
        except ZeroDivisionError:
            print("Skipping wrong value", num)
        except ValueError:
            print("Skipping wrong value", num)
        else:
            print("else block got executed")
        # except ZeoDivisionError
    print(numbers)
    return numbers

#function for adding the number.
def add():
  
    # '1,2,3,4,5,6,7,8,9,10'

    numbers = get_input()
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
    return sum

#function for Subtracting.
def sub():
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    sub = num1 - num2
    print(sub)
    return sub

#function for multiplication the number.
def mul():
    numbers_string = input("Enter comma separated integer value : ")
    # '1,2,3,4,5,6,7,8,9,10'
    numbers = get_input()
    prod = 1
    for num in numbers:
        prod = prod * num
    print(prod)
    return prod


def div():
    num1 = int(input("Enter Divisor"))
    num2 = int(input("Enter Dividend"))
    try:
        result = num2/num1
    except ZeroDivisionError:
        print("cannot divided by zero")



def square():
    num = int(input("Enter the number:\n"))
    square = num * num
    print(square)
    return square


def show_menu():
    '''
    Shows the list of available operations
    :return: None
    '''
    print('\n\n', '*' * 70)
    print("Choose from the following")
    print("1. Add")
    print("2. Subtract two numbers")
    print("3. Multiply")
    print("4. Divide")
    print("5. square")
    print("6. Exit the program")
    option = input("Enter your choice of operation to be performed : ")
    print('\n')
    if option == str(6):
        print("exiting the function")
        exit(0)
    elif option == str(5):
        square()
    elif option == str(4):
        div()
    elif option == str(3):
        mul()
    elif option == str(2):
        sub()
    elif option == str(1):
        add()
        # nums = input('user')
        # add(*args)


# option = input("Enter your choice of operation to be performed")
#

while True:
    show_menu()
   
