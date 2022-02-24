age = input('Enter your age plz (hours):')

first_digit = age[0]
second_digit = age[1]

age = int(age)

if age % 2 == 0:
    print('It\'s even!')
else:
    print('It\'s odd!')

if int(first_digit) % 2 == 0 or int(second_digit) % 2 == 0:
    print('It has an even digit!')
else:
    print('nope')