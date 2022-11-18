str_A = ""
for row in range(5):
    for column in range(6):
        if (
                ((row == 0 and 2 <= column <= 3)) or
                (row == 1 and (column == 1 or column == 4)) or
                ((row == 2 or row == 4) and (column == 0 or column == 5)) or
                (row == 3)
        ):
            str_A = str_A + "*"
        else:
            str_A = str_A + " "
    str_A = str_A + "\n"
#
letter_B = ""
for row in range(5):
    for column in range(6):
        if (
                (row == 0 and (0 <= column <= 3))
                or (row == 2 and (0 <= column <= 3))
                or (row == 4 and (0 <= column <= 3))
                or ((row == 1 or row == 3) and (column == 0 or column == 4))
        ):
            print("*", end="")
        else:
            print(end=" ")
    print()

letter_C = ""
for row in range(5):
    for column in range(6):
        if (
                ((row == 0 or row == 4))
                or (column == 0)):
            print("*", end="")

        else:
            print(end=" ")
    print()
#
letter_D = ""
for row in range(5):
    for column in range(6):
        if (
                ((row == 0 or row == 4) and (0 <= column <= 4))
                or
                ((1 <= row <= 3) and (column == 0 or column == 5))
        ):
            print("*", end="")

        else:
            print(end=" ")
    print()

letter_E = ""
for row in range(5):
    for column in range(6):
        if (

                (row % 2 == 0) or
                column == 0):
            letter_E = letter_E + "*"
        else:
            letter_E += " "
    letter_E += "\n"
print(letter_E)

letter_F = ""
for row in range(5):
    for column in range(6):
        if (
                (column == 0) or
                (row == 0 or row == 2)
        ):
            letter_F += "*"
        else:
            letter_F += " "
    letter_F = letter_F + "\n"
print(letter_F)

letter_G = ""
for row in range(5):
    for column in range(6):
        if (
                (column == 0) or (row == 0 or row == 4) or
                ((row == 2 or row == 3) and column == 5) or
                (row == 2 and (column == 3 or column == 4))
        ):
            letter_G = letter_G + "*"
        else:
            letter_G += " "
    letter_G += "\n"
print(letter_G)

letter_H = ""
for row in range(5):
    for column in range(6):
        if (
                ((row != 2) and (column == 0 or column == 5))
                or (row == 2)):
            print("*", end="")
        else:
            print(end=" ")
    print()

letter_I = ""

for row in range(5):
    for column in range(7):
        if (
                (row == 0)
                or (row == 4)
                or column == 3
        ):
            letter_I = letter_I + "*"
        else:
            letter_I += " "
    letter_I = letter_I + "\n"
print(letter_I)

letter_J = ""
for row in range(5):
    for column in range(7):
        if (
                (row == 0)
                or ((row == 4) and (0 <= column <= 4))
                or (column == 5)
        ):
            letter_J += "*"
        else:
            letter_J += " "
    letter_J = letter_J + "\n"
print(letter_J)

letter_K = ""
for row in range(7):
    for column in range(5):
        if (
                (column == 0) or (row == 3 and column == 1)
                or ((row == 4 or row == 2) and column == 2)
                or ((row == 1 or row == 5) and column == 3)
                or ((row == 0 or row == 6) and column == 4)):
            letter_K += "*"
        else:
            letter_K += " "
    letter_K = letter_K + "\n"
print(letter_K)

letter_L = ""
for row in range(5):
    for column in range(6):
        if (
                (column == 0) or (row == 4)
        ):
            letter_L += "*"
        else:
            letter_L += " "
    letter_L = letter_L + "\n"
print(letter_L)

letter_M = ""
for row in range(7):
    for column in range(7):
        if (
                (column == 0 or column == 6)
                or (row == 1 and (column == 1 or column == 5))
                or (row == 2 and (column == 2 or column == 4))
                or (row == 3 and (column == 3))
        ):
            letter_M += "*"
        else:
            letter_M += " "
    letter_M = letter_M + "\n"
print(letter_M)

letter_N = ""
for row in range(5):
    for column in range(6):
        if (
                (column == 0 or column == 5)
                or (column == 1 and row == 1)
                or (column == 2 and row == 2)
                or (row == 3 and column == 3)
                or (row == 4 and column == 4)):
            letter_N = letter_N + "*"
        else:
            letter_N += " "

    letter_N = letter_N + "\n"
print(letter_N)

letter_O = ""
for row in range(5):
    for column in range(6):
        if (
                ((row == 0 or row == 4) and (1 <= column <= 4))
                or (1 <= row <= 3 and (column == 0 or column == 5))
        ):
            letter_O += "*"
        else:
            letter_O += " "
    letter_O += "\n"
print(letter_O)

letter_P = ""
for row in range(5):
    for column in range(6):
        if (
                (column == 0)
                or (row == 0)
                or row == 2
                or (row == 1 and column == 5)
        ):
            letter_P += "*"
        else:
            letter_P += " "
    letter_P += "\n"
print(letter_P)

letter_Q = ""
for row in range(8):
    for column in range(5):
        if (
                (row == 0 and (1 <= column <= 3))
                or (1 <= row <= 4 and (column == 0 or column == 4))
                or (row == 5 and (column == 0 or column == 1 or column == 4))
                or (row == 6 and (1 <= column <= 3))
                or (row == 7 and column == 3)
        ):
            letter_Q += "*"
        else:
            letter_Q += " "
    letter_Q += "\n"
print(letter_Q)


letter_R = ""
for row in range(5):
    for column in range(6):
        if (
                ((row == 0 or row == 2) and (0 <= column <= 3))
                or ((row == 1 or row == 3) and (column == 0 or column == 4))
                or (row == 4 and (column == 0 or column == 5))

        ):
            letter_R += "*"
        else:
            letter_R += " "
    letter_R += "\n"
print(letter_R)


letter_S = ''
for row in range(5):
    for column in range(6):
        if(
               (row%2 == 0)
            or (row == 1 and column == 0)
            or (row == 3 and column ==5)
        ):
            letter_S += "*"
        else:
            letter_S += " "
    letter_S += "\n"
print(letter_S)




