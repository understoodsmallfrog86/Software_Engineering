with open("input.txt", encoding='utf-8') as f:
    lines = f.readlines()

print(f"Букв: {sum(c.isalpha() for line in lines for c in line)}")
print(f"Слов: {sum(len(line.split()) for line in lines)}")
print(f"Строк: {len(lines)}")