a ,b = 1,2
next = b
count = 1
while count < 10:
    print(next, end=" ")
    a,b = b,next
    count += 1
    next = a+b
print()

