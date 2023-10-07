"""
• P4.18 Write a program that prints a multiplication table, like this:
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
. . .
10 20 30 40 50 60 70 80 90 100

"""
def main():
    #for 10 rows
    for i in range(1, 11):
        #for 10 columns
        for j in range(1, 11):
          #usage of %d in aligning the spaces
            print(f"%5d" % (i * j), end='')
        #go to the next line with each iteration
        print()

if __name__ == "__main__":
    main()

