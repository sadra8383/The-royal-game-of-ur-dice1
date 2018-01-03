import random
n=input()
while n != 'done':
    if n == 'dice':
        s=0
        a = random.randint(1,4)
        b = random.randint(1,4)
        c = random.randint(1,4)
        d = random.randint(1,4)
    if a == 4:
        s=s+1
    if b == 4:
        s=s+1
    if c == 4:
        s=s+1
    if d == 4:
        s=s+1
    print(s)
    n = input()
        
