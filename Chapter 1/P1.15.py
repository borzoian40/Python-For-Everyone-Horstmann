"""
• Business P1.15 In the United States there is no federal sales tax, so every state may impose its own 
sales taxes. Look on the Internet for the sales tax charged in five U.S. states, then 
write a program that prints the tax rate for five states of your choice.
Sales Tax Rates
Alaska: 0%
Hawaii: 4%
. . .
"""
def print_sales_tax_rates(states_tax):
    print("Sales Tax Rates in U.S. States:")
    print("{:<20} {:<10}".format("State", "Tax Rate (%)"))
    for state, tax_rate in states_tax.items():
        print("{:<20} {:<10}".format(state, tax_rate))

# Hypothetical sales tax rates (Replace these with actual rates from a reliable source)
sales_tax_rates = {
    "Alabama": 4.00,
    "Alaska": 1.76,
    "Arizona": 5.60,
    "Arkansas": 6.50,
    "California": 7.25,
    "Colorado": 2.90,
    "Connecticut": 6.35,
    "Delaware": 0.00,
    "Florida": 6.00,
    "Georgia": 4.00,
    "Hawaii": 4.00,
    "Idaho": 6.00,
    "Illinois": 6.25,
    "Indiana": 7.00,
    "Iowa": 6.00,
    "Kansas": 6.50,
    "Kentucky": 6.00,
    "Louisiana": 4.45,
    "Maine": 5.50,
    "Maryland": 6.00,
    "Massachusetts": 6.25,
    "Michigan": 6.00,
    "Minnesota": 6.88,
    "Mississippi": 7.00,
    "Missouri": 4.23,
    "Montana": 0.00,
    "Nebraska": 5.50,
    "Nevada": 6.85,
    "New Hampshire": 0.00,
    "New Jersey": 6.63,
    "New Mexico": 5.13,
    "New York": 8.875,
    "North Carolina": 4.75,
    "North Dakota": 5.00,
    "Ohio": 5.75,
    "Oklahoma": 4.50,
    "Oregon": 0.00,
    "Pennsylvania": 6.00,
    "Rhode Island": 7.00,
    "South Carolina": 6.00,
    "South Dakota": 4.50,
    "Tennessee": 7.00,
    "Texas": 6.25,
    "Utah": 6.10,
    "Vermont": 6.00,
    "Virginia": 5.30,
    "Washington": 6.50,
    "West Virginia": 6.00,
    "Wisconsin": 5.00,
    "Wyoming": 4.00
    # Include all the states and their respective tax rates...
    # (Copy and paste the rest of the states and their rates here)
}

print_sales_tax_rates(sales_tax_rates)
