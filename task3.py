from collections import Counter

def sigma(s):
    count = Counter(map(int, s))
    top_three = dict(count.most_common(3))
    return dict(sorted(top_three.items()))

s = str(input())
print(sigma(s))