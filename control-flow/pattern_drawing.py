pattern_size = int(input("Enter the size of the pattern:"))

first_line = 1

while first_line <= pattern_size:
    for _ in range(pattern_size):
        print("*", end="")
    print()
    first_line += 1