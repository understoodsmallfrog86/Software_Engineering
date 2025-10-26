def censor_text():
    with open('Запрещёные_слова.txt', encoding='utf-8') as f:
        forbidden = set(f.read().split())

    text = """Hello, world! Python IS the programming language of thE future. 
My EMAIL is....
PYTHON is awesome!!!!"""

    for word in forbidden:
        text = text.replace(word, '*' * len(word))
    print(text)


censor_text()