# P1.13 Wrtie a program that prints the United States flag, using * and = characters.

#We define two for loops; the first one for "rows" and the second one for "columns".
#




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
