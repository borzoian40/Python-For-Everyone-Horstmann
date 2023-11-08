"""
•• P2.6 Write a program that prompts the user for a measurement in meters and 
then converts it to miles, feet, and inches.
"""
def meters_to_miles_feet_inches(meters):
    # 1 meter = 0.000621371 miles
    # 1 meter = 3.28084 feet
    # 1 meter = 39.3701 inches

    # Conversion factors
    meters_to_miles = 0.000621371
    meters_to_feet = 3.28084
    meters_to_inches = 39.3701

    # Conversion calculations
    miles = meters * meters_to_miles
    feet = meters * meters_to_feet
    inches = meters * meters_to_inches

    return miles, feet, inches

def main():
    meters = float(input("Enter a measurement in meters: "))

    miles, feet, inches = meters_to_miles_feet_inches(meters)

    print(f"{meters} meters is equal to:")
    print(f"{miles:.5f} miles")
    print(f"{feet:.2f} feet")
    print(f"{inches:.2f} inches")

if __name__ == "__main__":
    main()
