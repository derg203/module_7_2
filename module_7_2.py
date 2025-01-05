def custom_write(file_name: str, strings: list):
    strings_positions = {}
    line_number = 1
    file = open(file_name, 'w', encoding="utf-8")
    for i in strings:
        byte = file.tell()
        file.write(f'{i}\n')
        strings_positions[(line_number, byte)] = i
        line_number += 1
    file.close()
    return strings_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]
    result = custom_write('test.txt', info)
    for i in result.items():
        print(i)