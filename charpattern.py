n = chr(input())
for i in range(n):
    for  j in range(n):
        print("ord(value)+1", end = ' ')
    print()


for i in range(5):  # 5 rows
    for j in range(5):  # 5 columns
        print(chr(65 + j), end=" ")
    print()

for i in range(5):  # 5 rows
    for j in range(5):  # 5 columns
        print(chr(65 + i), end=" ")
    print()

