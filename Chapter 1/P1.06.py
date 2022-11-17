#Write a program that prints your name in large letters, such as the following below
str_A = ""
for row in range(5):
    for column in range(6):
        if ((row == 0 and 2<=column<=3)) or (row ==1 and (column==1 or column ==4)) or ((row ==2 or row==4) and (column==0  or column ==5)) or(row==3):
            str_A = str_A + "*"
        else:
            str_A = str_A + " "
    str_A = str_A + "\n"

letter_B = ""
for row in range(5):
    for column in range(6):
        if (row== 0 and (0<=column<=3)) or (row == 2 and(0<=column<=3)) or (row == 4 and(0<=column<=3)) or ((row==1 or row == 3) and(column == 0 or column == 4) ) :
            print("*", end = "")
        else:
            print(end= " ")
    print()
    
    
letter_C=""
for row in range(5):
    for column in range(6):
        if ((row == 0 or row == 4)) or (column==0):
            print("*", end = "")
        else:
            print(end = " ")
    print()
#
letter_D = ""
for row in range(5):
    for column in range(6):
        if ((row == 0 or row==4) and (0<=column<=4)) or ((1<=row<=3) and (column==0 or column == 5)):
            print("*", end = "")
        else:
            print(end = " ")
    print()

letter_E = ""
for row in range(5):
    for column in range(6):
        if ((row%2==0)) or column == 0:
            letter_E = letter_E + "*"
        else:
            letter_E += " "
    letter_E += "\n"
print(letter_E)


letter_F = ""
for row in range(5):
    for column in range(6):
        if ((column == 0) or (row == 0 or row == 2)):
            letter_F += "*"
        else:
            letter_F += " "
    letter_F = letter_F + "\n"
print(letter_F)


letter_G = ""
for row in range(5):
    for column in range(6):
        if (column ==0) or (row==0 or row == 4) or((row == 2 or row == 3) and column==5) or (row==2 and (column==3 or column==4)):
            letter_G = letter_G + "*"
        else:
            letter_G += " "
    letter_G += "\n"
print(letter_G)

# letter_H = ""
# for row in range(5):
#     for column in range(6):
#         if(((row == 0 or row == 1 or row == 3 or row == 4) and (column == 0 or column == 5)) or (row==2)):
#             print("*", end = "")
#         else:
#             print(end = " ")
#     print()

letter_I = ""

for row in range(5):
    for column in range(7):
        if(row==0) or (row == 4) or column == 3:
            letter_I = letter_I + "*"
        else:
            letter_I+= " "
    letter_I = letter_I + "\n"
print(letter_I)

letter_J = ""
for row in range(5):
    for column in range(7):
        if (row == 0)  or ((row==4) and (0<=column<=4)) or (column == 5):
            letter_J += "*"
        else:
            letter_J += " "
    letter_J = letter_J + "\n"
print(letter_J)


letter_K = ""
for row in range(5):
    for column in range(7):
        if(column == 0) or ((row==0 or row== 4) and (column == 6)) or ((row == 1 or row ==3) and (column == 2)):
            letter_K += "*"
        else:
            letter_K += " "
    letter_K = letter_K + "\n"
print(letter_K)
