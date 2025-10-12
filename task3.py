one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

one.sort()
two.sort()
three.sort()

def geron(a,b,c):
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    return(s)

print("one", geron(one[0],one[1],one[2]), geron(one[2], one[3], one[4]))
print("two", geron(two[0],two[1],two[2]), geron(two[2], two[3], two[4]))
print("three", geron(three[0],three[1],three[2]), geron(three[2], three[3], three[4]))
