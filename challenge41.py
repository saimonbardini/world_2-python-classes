from datetime import date

current_year = date.today().year
birth_age = int(input('insert your age of birth: '))
age = current_year - birth_age

if birth_age < current_year:
    if age < 9:
        category = 'Mirim'
    elif 10 <= age < 14:
        category = 'Infantil'
    elif 15 <= age <= 19:
        category = 'Junior'
    elif age == 20:
        category = 'Sênior'
    elif age >= 21:
        category = 'Master'
    print(category)

else:
    print('you hevent been born yet')