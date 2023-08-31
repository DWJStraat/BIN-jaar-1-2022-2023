# Original version
# a = 70*6
# b = 70*10
# c = 70*15
# print(f'A car is traveling at 70 miles per hour.')
# print(f'If the car is traveling for 6 hours, the distance traveled is {a} miles.')
# print(f'If the car is traveling for 10 hours, the distance traveled is {b} miles.')
# print(f'If the car is traveling for 15 hours, the distance traveled is {c} miles.')

# Rewritten version
speed = 70
time = [6, 10, 15]
print (f'A car is traveling at {speed} miles per hour.')
for i in time:
    print(f'If the car is traveling for {i} hours, the distance traveled is '
          f'{speed * i} miles.')
