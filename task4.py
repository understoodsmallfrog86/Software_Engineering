a=[2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
b=[4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
c=[5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]


def goodDnevnik(a):
    b=[]
    for i in range(len(a)):
        if a[i]!=2:
            if a[i]==3:
                b.append(4)
            else:
                b.append(a[i])
    return b



print(goodDnevnik(a))
print(goodDnevnik(b))
print(goodDnevnik(c))
