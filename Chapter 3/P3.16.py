"""
•• P3.16 Write a program that reads in three strings and sorts them lexicographically.
Enter a string: Charlie 
Enter a string: Able 
Enter a string: Baker 
Able
Baker 
Charlie
"""
def main():
    number_names = int(input("How many names would you like: "))
    list = []
    for i in range(number_names):
        str = input(f"{i+1}: ")
        list.append(str)

    new_lists = sorted(list)
    for i in range(number_names):
        print(new_lists[i])
      
if __name__ == "__main__":
    main()

