# a
for i in range(0, 100 + 1, 10):
    print(i, end=" ")
print()

# b
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c
number_of_stars = int(input("How many stars do you want: "))
for i in range(number_of_stars):
    print("*", end="")
print()

# d
for i in range(number_of_stars):
    for j in range(i + 1):
        print("*", end="")
    print()
