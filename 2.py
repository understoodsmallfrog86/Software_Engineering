def read_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()

        if not content:
            raise Exception("Файл пустой")

        return content

    except FileNotFoundError:
        return "Файл не найден"
    except Exception as e:
        return str(e)


file1_content = read_file_content('data.txt')
print(file1_content)

file2_content = read_file_content('empty.txt')
print(file2_content)