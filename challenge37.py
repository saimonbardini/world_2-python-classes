num = int(input('insert a number: '))
print("""choices:
1 - to binary.
2 - to octal.
3 - to hexadecimal.""")
choice = int(input('insert your choice: '))

if choice == 1:
    num = bin(num)
elif choice == 2:
    num = oct(num)
elif choice == 3:
    num = hex(num)

print(num)