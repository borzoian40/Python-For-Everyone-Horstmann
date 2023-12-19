"""
•• P8.17 Write a program that readsthe data from https://www.cia.gov/library/publications/
the-world-factbook/rankorder/rawdata_2004.txt into a dictionary whose keys are 
country names and whose values are per capita incomes. Then the program should 
prompt the user to enter country names and print the corresponding values. Stop 
when the user enters quit.
"""
def read_data(file_path):
    data_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Splitting the line into two parts: index_and_country, income
            index_and_country, income = line.strip().split('$', 1)
            #print(f"Index and Country: {index_and_country}, Income: {income}")

            index, country = index_and_country.split(maxsplit=1)
            #print(f"Index: {index}, Country: {country}")

            # Removing commas from income and converting to float
            income = float(income.replace(",", ""))
            #print(f"Cleaned Income: {income}")
            countrynames = country.strip()
            data_dict[countrynames] = income

    return data_dict


def main():
    file_path = 'justyouknow.txt'
    data_dict = read_data(file_path)


    while True:
        print("Available country names:", list(data_dict.keys()))
        user_input = input("Enter a country name (or 'quit' to exit): ").strip()
        if user_input.lower() == 'quit':
            break

        if user_input in data_dict:
            print(f"The per capita income for {user_input} is: {data_dict[user_input]}")
        else:
            print(f"Country '{user_input}' not found in the data. Please try again.")


if __name__ == "__main__":
    main()
