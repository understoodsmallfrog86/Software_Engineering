list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def sigma(a):
    b=set()
    for i in range(len(a)):
        if a[i] in b:
            c=str(a[i])*2
            while c in b:
                c+=str(a[i])
            b.add(c)
        else: b.add(a[i])
    return b
print(sigma(list_1))
