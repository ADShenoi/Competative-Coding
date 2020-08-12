import numpy as np


def is_prime(n):
    sqt = int(np.sqrt(n))
    for j in range(2, sqt):
        if n % j == 0:
            return False
    return True


c = 0
for i in range(99999, 10000, -1):
    x = str(i)
    x += x[-2::-1]
    x = int(x)
    if is_prime(x):
        c += 1
        print(x)
        if c >= 3:
            exit()
