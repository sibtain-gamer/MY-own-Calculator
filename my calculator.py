print("Hello to this simple calculator by Gamer_Sibtain")

first_num = float(input('Enter the first number '))
second_num = float(input('Enter the second number '))

operator = str(input('Enter what you want to do \n +,\n - ,\n * ,\n / '))

if operator == '+':
    print(first_num + second_num)

elif operator == '-':
    print(first_num - second_num)

elif operator == '*':
    print(first_num * second_num)

elif operator == "/":
    print(first_num / second_num)

