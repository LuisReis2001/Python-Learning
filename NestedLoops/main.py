
# Nested Loops -> The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop".

rows = int(input("How many rows: "))
cols = int(input("How many columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end = "")     #Print in the same lane
    print()