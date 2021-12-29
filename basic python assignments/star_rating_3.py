# printing star rating pattern
Rows = 5
for i in range(0, Rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
