l1 = int(input("How long is rectangle 1?\n"))
w1 = int(input("How wide is rectangle 1?\n"))
r1 = l1 * w1
l2 = int(input("How long is rectangle 2?\n"))
w2 = int(input("How wide is rectangle 2?\n"))
r2 = l2 * w2

if r1 > r2:
    dif = "larger"
elif r2 > r1:
    dif = "smaller"
elif r1 == r2:
    dif = "equal"
    
print(f"The first rectangle, being {r1}, is {dif} than the second, being {r2}")