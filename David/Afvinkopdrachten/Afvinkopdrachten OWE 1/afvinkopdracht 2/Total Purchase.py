a=float(input('What is the price of the first object in $?\n'))
b=float(input('What is the price of the second object in $?\n'))
c=float(input('What is the price of the third object in $?\n'))
d=float(input('What is the price of the fourth object in $?\n'))
e=float(input('What is the price of the fifth object in $?\n'))

subtotal = a+b+c+d+e

salestax = subtotal*0.07

total = subtotal+salestax

print(f'The subtotal is ${subtotal:.2f}. Adding ${salestax:.2f} in salestax, the total price is ${total:.2f}.\nHave a nice day, and please come again!')