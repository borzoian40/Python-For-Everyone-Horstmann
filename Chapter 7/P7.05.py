"""
Write a program that asksthe user for a file name and prints the number of characters, words,
and lines in that file
"""
def count_chars_words_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

            # Count characters
            char_count = len(content)

            # Count words
            word_count = len(content.split())

            # Count lines
            line_count = content.count('\n') + 1  # Assumes that the last line may not end with a newline

            print(f"Number of characters: {char_count}")
            print(f"Number of words: {word_count}")
            print(f"Number of lines: {line_count}")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

def main():
    file_name = input("Enter the file name: ")
    count_chars_words_lines(file_name)

if __name__ == "__main__":
    main()

