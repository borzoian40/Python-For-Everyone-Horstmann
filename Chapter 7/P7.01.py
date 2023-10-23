"""
 P7.1 Write a program that carries out the following tasks:
Open a filewith the name hello.txt.
Store the message “Hello,World!” in the file. 
Close the file.
Open the same file again.
Read the message into a string variable and print it.
"""
FILENAME = 'P7.01.txt'

def main():
    with open(FILENAME, "w") as my_file:
        my_file.write("Hello, World!")

    with open(FILENAME, "r") as my_file:
        message = my_file.read()

    print(message)

if __name__ == "__main__":
    main()
