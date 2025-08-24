n = int(input("Enter the number of rows: \n"))
print("Half pyramid pattern of stars (*): ")

for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()