r1 = float(input('input length: '))
r2 = float(input('input length: '))
r3 = float(input('input length: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    condition = 'can'
    if r1 == r2 ==r3:
        type = 'equilateral'
    elif r1 != r2 != r3 != r1:
        type = 'scalene'
    else:
        type = 'isosceles'
else:
    condition = 'cannot'
    type =''

print(f"they {condition} form a triangle {type}.")