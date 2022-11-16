#In the United States there is no federal sales tax, so every state may impose its own sales taxes.\
#Look on the Internet for tax sales tax charged in five U.S. states, then write a program that prints the tax rate for fives tates of your choice.



#from prettytable import PrettyTable
from tabulate import tabulate


states_taxes = [["Alabama", 4.00], ["Alaska", 0.00], ["Arizona", 5.60], ["Arkansas", 6.50],
        ["California", 7.25],["Colorado", 2.90], ["Connecticut", 6.35],
        ["Delaware", 0.00], ["D.C.", 6.00],
        ["Florida", 6.00],
        ["Georgia", 4.00],
        ["Hawaii", 4.00],
        ["Idaho", 6.00], ["Illinois", 6.25], ["Indiana", 7.00], ["Iowa", 6.00],
        ["Kansas", 6.50], ["Kentucky", 6.00],
        ["Louisiana", 4.45],
        ["Maine", 5.50], ["Maryland", 6.00], ["Massachusetts", 6.25], ["Michigan", 6.00],
        ["Minnesota", 6.875], ["Mississippi", 7.00], ["Missouri", 4.225], ["Montana", 0.00],
        ["Nebraska", 5.50], ["Nevada", 6.85], ["New Hampshire", 0.00],
        ["New Jersey", 6.625], ["New Mexico", 5.125], ["New York", 4.00],
        ["North Carolina", 4.75], ["North Dakota", 5.00],
        ["Ohio", 5.75], ["Oklahoma", 4.50], ["Oregon", 0.00],
        ["Pennsylvania", 6.00], ["Rhode Island", 7.00],
        ["South Carolina", 6.00], ["South Dakota", 4.50],
        ["Tennessee", 7.00], ["Texas", 6.25],
        ["Utah", 6.10],
        ["Vermont", 6.00], ["Virginia", 5.30],
        ["Washington", 6.50], ["West Virginia", 6.00], ["Wisconsin", 6.00], ["Wyoming", 4.00]]

# Add rows
# myTable.add_row(["Alabama", "91.2 %"])
# myTable.add_row(["Alaska", "63.5 %"])
# myTable.add_row(["Arizona", "90.23 %"])
# myTable.add_row(["Arkansas", "92.7 %"])
# myTable.add_row(["California", "98.2 %"])
# myTable.add_row(["Colorado", "88.1 %"])
# myTable.add_row(["Connecticut",  "95.0 %"])
columns_name = ["States", "Tax Rate"]

print(tabulate(states_taxes, headers= columns_name, tablefmt='fancy_grid', showindex = range(1,52)))
