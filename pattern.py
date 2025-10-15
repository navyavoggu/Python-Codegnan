import string
letters=list(string.ascii_uppercase)
small_letters=list(string.ascii_lowercase)
for i in range(0,26,3):
    for j in range(3):
        if i+j<26:
            print(f"{letters[i+j]}{small_letters[i+j]}",end="\t")
    print()
    
