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
