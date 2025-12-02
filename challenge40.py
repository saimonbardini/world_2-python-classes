assessment1 = float(input('insert your first note: '))
assessment2 = float(input('insert your second note: '))

average = (assessment1 + assessment2) / 2

if average < 5.0:
    print('REPROVED')
elif 5<= average < 6.9:
    print('RECUPERATION')
elif average > 7:
    print('APPROVED')