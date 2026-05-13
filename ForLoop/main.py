
import time

# For loop -> A statement that will execute it's block of code with limited amount of time.

for i in range(10):
    print(i + 1)

for i in range(50, 101, 2):
    print(i)

for i in "Luis Reis":
    print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)

print("Happy New Year")