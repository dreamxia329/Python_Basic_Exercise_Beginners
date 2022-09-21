print('Just enter any two numbers for multiplying.')
print("To exit, enter 'e'")
while True:
    try:
        num1 = input('\nnum1: ')
        if num1 == 'e':
            break
        num2 = input('num2: ')
        if num2 == 'e':
            break

        result = int(num1) * int(num2)
        print('Answer:' + str(result))
    except ValueError:
        print('Oops! You can only enter numerical.')  # use 'pass' to ignore errors.
