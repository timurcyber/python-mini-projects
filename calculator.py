def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def div(a, b):
    if b == 0:
        print("Division by zero is not allowed!")
        return
    print(a / b)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Hey, enter a NUMBER!')

while True:
    print('A. Add')      
    print('B. Subtract')      
    print('C. Multiply')      
    print('D. Divide')      
    print('E. Exit')    

    choice = input('Choose an operator: ').lower()

    if choice == 'a':
        print('Addition')
        a = get_int('Enter first number: ')
        b = get_int('Enter second number: ')
        add(a, b)

    elif choice == 'b':
        print('Substract')
        a = get_int('Enter first number: ')
        b = get_int('Enter second number: ')
        sub(a, b)

    elif choice == 'c':
        print('Multiply')
        a = get_int('Enter first number: ')
        b = get_int('Enter second number: ')
        multiply(a, b)

    elif choice == 'd':
        print('Divide')
        a = get_int('Enter first number: ')
        b = get_int('Enter second number: ')
        div(a, b)

    elif choice == 'e':
        print('Goodbye!')
        break

    else:
        print('Invalid choice. Please select a valid option!')
