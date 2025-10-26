import re
from collections import Counter

with open("statia.txt", encoding='utf-8') as f:
    words = re.findall(r'\w+', f.read().lower())

print(f"Общее количество слов: {len(words)}")
print(f"Самое частое слово: '{Counter(words).most_common(1)[0][0]}'")