"""
• P5.9 Write functions
def sphereVolume(r) 
def sphereSurface(r)
def cylinderVolume(r, h) 
def cylinderSurface(r, h) 
def coneVolume(r, h)
def coneSurface(r, h)
that compute the volume and surface area of a sphere with radius r, a cylinder with a 
circular base with radius r and height h, and a cone with a circular base with radius r 
and height h. Then write a program that prompts the user for the values of r and h, 
calls the six functions, and prints the results
"""
import math

# Function to calculate the volume of a sphere
def sphereVolume(r):
    return (4/3) * math.pi * r**3

# Function to calculate the surface area of a sphere
def sphereSurface(r):
    return 4 * math.pi * r**2

# Function to calculate the volume of a cylinder
def cylinderVolume(r, h):
    return math.pi * r**2 * h

# Function to calculate the surface area of a cylinder
def cylinderSurface(r, h):
    return 2 * math.pi * r**2 + 2 * math.pi * r * h

# Function to calculate the volume of a cone
def coneVolume(r, h):
    return (1/3) * math.pi * r**2 * h

# Function to calculate the surface area of a cone
def coneSurface(r, h):
    l = math.sqrt(r**2 + h**2)  # Slant height
    return math.pi * r * (r + l)

def main():
    r = float(input("Enter the radius (r): "))
    h = float(input("Enter the height (h): "))

    sphere_vol = sphereVolume(r)
    sphere_surf = sphereSurface(r)
    cylinder_vol = cylinderVolume(r, h)
    cylinder_surf = cylinderSurface(r, h)
    cone_vol = coneVolume(r, h)
    cone_surf = coneSurface(r, h)

    print(f"Volume of the sphere: {sphere_vol:.2f}")
    print(f"Surface area of the sphere: {sphere_surf:.2f}")
    print(f"Volume of the cylinder: {cylinder_vol:.2f}")
    print(f"Surface area of the cylinder: {cylinder_surf:.2f}")
    print(f"Volume of the cone: {cone_vol:.2f}")
    print(f"Surface area of the cone: {cone_surf:.2f}")

if __name__ == "__main__":
    main()
