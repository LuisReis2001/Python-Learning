
# Loop Control Statements -> Change a loop execution from its normal sequence.

# Break -> Terminate the loop entirely
# Continue -> Skips to the next iteration of the loop
# Pass -> Acts as a placeholder

# Break use

while True:
    name = input("Enter your name: ")
    if name != "":
        break

# Continue

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end = "")

# Pass

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)

