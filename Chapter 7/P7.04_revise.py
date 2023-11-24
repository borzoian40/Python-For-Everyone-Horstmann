"""
P7.4 Write a program that reads a file containing two columns of floating-point numbers. 
Prompt the user for the file name. Print the average of each column.
"""
def read_file_and_calculate_average(file_name):
    try:
        with open(file_name, 'r') as file:
            column1_sum = 0
            column2_sum = 0
            count = 0

            for line in file:
                # Assuming the columns are separated by whitespace
                columns = line.split()
              """
              column1, column2 = map(float, line.split())
              """
                if len(columns) == 2:
                    column1_sum += float(columns[0])
                    column2_sum += float(columns[1])
                    count += 1

            if count > 0:
                avg_column1 = column1_sum / count
                avg_column2 = column2_sum / count
                print(f"Average of Column 1: {avg_column1:.2f}")
                print(f"Average of Column 2: {avg_column2:.2f}")
            else:
                print("No data found in the file.")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except ValueError:
        print("Error: Invalid data format in the file.")

def main():
    file_name = input("Enter the file name: ")
    read_file_and_calculate_average(file_name)

if __name__ == "__main__":
    main()
