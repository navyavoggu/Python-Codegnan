n = int(input())
i = 1
while i<=n:
    if n % 7 == 0:
        print(i)
        break
    i +=1
else:
    print("not found")
