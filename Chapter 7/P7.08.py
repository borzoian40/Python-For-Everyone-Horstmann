"""
•• P7.8 Write a program that replaces each line of a file with its reverse. For example, if you run
python reverse.py hello.py
then the contents of hello.py are changed to
.margorp nohtyP tsrif yM #
)"!dlroW ,olleH"(tnirp
Of course, if you run Reverse twice on the same file, you get back the original file
"""
def reverse_lines(input_file, output_file):
    try:
        # Read lines from the input file
        with open(input_file, 'r') as input_file:
            lines = input_file.readlines()

        # Reverse each line
        reversed_lines = [line.strip()[::-1] + '\n' for line in lines]

        # Write the reversed lines to the output file
        with open(output_file, 'w') as output_file:
            output_file.writelines(reversed_lines)

        print(f"Lines reversed and written to '{output_file}' successfully.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # Input and output file names
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    reverse_lines(input_file, output_file)


if __name__ == "__main__":
    main()
