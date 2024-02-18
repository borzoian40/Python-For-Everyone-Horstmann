FILENAME = "morse_code.txt"
COMMAND = "command.txt"


def read_morseTable(filepath):
    table_morse = {}
    try:
        with open(filepath, 'r') as files:
            for row in files:
                character, code = row.strip().split(' ', 1)
                table_morse[character] = code

    except FileNotFoundError:
        print("Well ... it seems the file doesn't exist.")

    return table_morse


def encode_text(text_line, morse_table):
    list_text = []

    for every_character in text_line:
        every_character = every_character.upper()
        if every_character in morse_table:
            list_text.append(morse_table[every_character])
    return ' '.join(list_text)


def decode_text(morse_line, morse_table):
    list_decode = []

    symbols = morse_line.split()

    for every_symbol in symbols:
        for character, code in morse_table.items():
            if code == every_symbol:
                list_decode.append(character)

    return ''.join(list_decode)


def main():
    read_Table = read_morseTable(FILENAME)

    try:
        with open(COMMAND, 'r') as file:
            for row in file:
                command, filename = row.strip().split()
                with open(filename, 'r') as in_file:
                    operations = in_file.read().strip()

                if command == 'c':
                    answer = encode_text(operations, read_Table)
                    print(f"Encoded text: {answer}")
                elif command == 'd':
                    answer = decode_text(operations, read_Table)
                    print(f"Decoded text: {answer}")

    except FileNotFoundError:
        print(f"Hello: its wrong and there is no file")


if __name__ == "__main__":
    main()
