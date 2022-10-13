cookies = int(input('How many cookies would you like to bake?\n'))

sugar = 1.5/48*cookies
butter = 1/48*cookies
flour = 2.75/48*cookies

print(f'To bake {cookies} amount of cookies, you need:')
print(f'\t-{sugar:.2f} cups of sugar')
print(f'\t-{butter:.2f} cups of butter')
print(f'\t-{flour:.2f} cups of flour')
print('')
print('Bon appetit :)')