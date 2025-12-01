from datetime import date

current_year = date.today().year
birth_age = int(input('insert your age of birth: '))
age = current_year - birth_age

if birth_age < current_year:
    if age < 18:
        print('you will still enlist.')
        print(f'missing {18 - age} years')
    elif age == 18:
        print('its time of enlist.')
    elif age > 18:
        print('its past time to enlist')
        print(f'it happened {age - 18} years.')
else:
    print('you havent been born yeat.')