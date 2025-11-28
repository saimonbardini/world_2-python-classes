home_value = float(input('insert the home value: R%'))
salary = float(input('insert your salary: R$'))
years = int(input('number of years: '))

provision = home_value / (years * 12)
percent = salary * (30 / 100)

if provision < percent:
    print('loan approved')
    print(f'your installment: R${provision}')
else:
    print('loan denied')