"""
• P8.2 Write a program that counts how often each word occurs in a text file.
"""
def count_word_occurrences(file_name):
    word_count = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip('.,!?\'"(){}[]').lower()
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1
    except FileNotFoundError:
        print("File not found.")
        return word_count

    return word_count

def main():
    file_name = 'who_knows.txt'  # Replace with your file name or path
    word_count = count_word_occurrences(file_name)

    if word_count:
        for word, count in word_count.items():
            print(f'Word: {word}, Count: {count}')

if __name__ == "__main__":
    main()
