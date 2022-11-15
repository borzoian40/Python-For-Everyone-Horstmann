# P1.13 Wrtie a program that prints the United States flag, using * and = characters.

#We define two for loops; the first one for "rows" and the second one for "columns".
#Now for the stars, the program prints them only when the sum of indices of rows and columns are even, otherwise it prints a "space"(i.e. " ") 
#and moves on to the next index.
#at the end of the first for loop we use print() so that the program goes to the next line and prints the rest of the remaining elements of our U.S. flag.

#REMEMEBR: THE AMERICAN FLAG HAS 50 STARS EACH OF THEM REPRESENTING A STATE.

def main():
    for i in range(0, 15):
        for j in range(0, 46):
            if (i < 9 and j < 12):
                if ((i + j) % 2 == 0 and j != 11):
                    print("*", end='')
                else:
                    print(" ", end='')

            else:
                print("=", '')
        print()


if __name__ == "__main__":
    main()
    


    
    
#P.S. The idea and algorithm of the above code was taken from this website: https://petamind.com/fun-coding-challenge-print-the-american-flag/

