from typing import final

tuple=(1,2,3,3,1,2)
l=int(input())
try:
    a=tuple.index(l)
except: a=None
try:
    b=tuple.index(l,a+1)
except:
    b=None
if b!= None:
    print(tuple[a:b+1])
elif a!=None: print(tuple[a:])
else: print("нет")