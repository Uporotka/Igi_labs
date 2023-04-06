def arithmetic_operation(first_number, second_number, operation):
    if(operation == 'add'):
        return first_number + second_number
    elif (operation == 'sub'):
        return first_number - second_number
    elif (operation == 'mult'):
        return first_number * second_number
    elif (operation == 'div'):
        return first_number / second_number
    else:
        return 'faulse'

def checkNumber(number):
    while True:
        if number.isdigit():
            return int(number)
        else:
            print("No.. input is not a number.")
            number = input("try again: ")

def checkString(str):
    while True:
        if str == 'add' or str == 'sub' or str =='mult'or str == 'div':
            return str
        else:
            print("No.. input is not a correct.")
            str = input("try again: ")



print("Hellow world")
print()


first_number = checkNumber(input("Enter the first number: "))
second_number = checkNumber(input("Enter the second number: "))
operation = checkString(input("Enter operation(string like “add”, “sub”, “mult” and “div”): "))
print("result: ", arithmetic_operation(first_number,second_number,operation))
print()

