# Write a program that prints the balance of an account after the first, second, and third year. 
#The account has an initial balance of $1,000 and earns 5 percent interest per year

salary = 1000
rate = 0.05

year0 = salary
year1 = salary*rate + year0
year2 = year1*rate + year0
year3 = year2*rate + year0

print(f"Current balance of first year: {year1} $")
print(f"Current balance of second year: {year2} $")
print(f"Current balance of third year: {year3} $")
