"""
 P2.7 Write a program that prompts the user for a radius and then prints
• The area and circumference of a circle with that radius
• The volume and surface area of a sphere with that radius
"""
import math

def main():
    radius = float(input("Please enter the radius: "))
    # A
    area = (math.pi) * (radius ** 2)
    circumference = 2 * (math.pi) * radius

    # B
    volume = 4 / 3 * (math.pi) * (radius ** 3)
    surface_area = 4 * (math.pi) * (radius ** 2)

    print("A)")
    print(f"Area of a circle:{area:10.3f}")
    print(f"Circumference:{circumference:13.3f}")
    print()
    print("B)")
    print(f"Volume of a Sphere:{volume:10.3f}")
    print(f"Surface Area:{surface_area:15.3f}")


if __name__ == "__main__":
    main()
