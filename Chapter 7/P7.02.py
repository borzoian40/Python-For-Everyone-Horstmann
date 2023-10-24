"""
• P7.2 Write a program that reads a file containing text. Read each line and send it to the 
output file, preceded by line numbers. If the input file is
Mary had a little lamb
Whose fleece was white as snow. 
And everywhere that Mary went, 
The lamb was sure to go!
then the program produces the output file
/* 1 */ Mary had a little lamb
/* 2 */ Whose fleece was white as snow.
/* 3 */ And everywhere that Mary went,
/* 4 */ The lamb was sure to go!
Prompt the user for the input and output file 
names
"""

def main():
    # Prompt the user for input and output file names
    input_file_name = input("Enter the name of the input file: ")
    output_file_name = input("Enter the name of the output file: ")

    try:
        # Open the input file for reading
        with open(input_file_name, "r") as input_file:
            # Read the lines from the input file
            lines = input_file.readlines()

        # Open the output file for writing
        with open(output_file_name, "w") as output_file:
            # Write each line with line numbers to the output file
            for line_number, line in enumerate(lines, 1):
                # Format the line with line number and write to the output file
                formatted_line = f"/* {line_number} */ {line}"
                output_file.write(formatted_line)

        print(f"Lines with line numbers have been written to {output_file_name}")

    except FileNotFoundError:
        print("File not found. Please make sure the input file exists.")
    

if __name__ == "__main__":
    main()
