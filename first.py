def print_name(name):
    if name:
        print(name, 'is bad... psyche')

print_name('Ilia')

age = 13

def get_dog_years(age):
    if age < 2:
        return 'Age must be over two to work'
    elif age >= 2:
        return str(24 + (age - 2) * 4)

print(get_dog_years(age))

val_1 = 1

val_1 = input('Value 1: ')
val_2 = input('Value 2: ')
operation = input('Operation(mul, min...): ')

def calculator():
    if operation == 'mul':
        print(val_1 * val_2)
    elif operation == 'div':
        print(val_1 / val_2)
    elif operation == 'min':
        print(val_1 - val_2)
    elif operation == 'add':
        print(val_1 + val_2)

calculator()
