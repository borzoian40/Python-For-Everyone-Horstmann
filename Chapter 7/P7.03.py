"""
• P7.3 Repeat Exercise • P7.2, but allow the user to specify the file name on the command 
line. If the user doesn’t specify any file name, then prompt the user for the name.
"""
def main():
    input_file_name = input("Please enter the name of your input file: ")
    output_file_name = input("Please enter the name of your output file: ")

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

        print(f"Lines with line numbers have been written to \'{output_file_name}\'")
        

    except FileNotFoundError:
        print("File not found. Please make sure the input file exists.")

if __name__ == "__main__":
    main()
