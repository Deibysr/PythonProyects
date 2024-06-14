import math

def find_angle_MBC(AB, BC):
    # Calculate the hypotenuse AC
    AC = math.sqrt(AB**2 + BC**2)
    
    # Since M is the midpoint of AC, BM is half of AC
    BM = AC / 2
    
    # Calculate the angle MBC using the sine rule
    # sin(theta) = AB / AC
    angle_MBC_radians = math.asin(AB / AC)
    angle_MBC_degrees = math.degrees(angle_MBC_radians)
    
    # Round the angle to the nearest integer
    angle_MBC = round(angle_MBC_degrees)
    
    return angle_MBC

# Sample input
AB_length = float(input())
BC_length = float(input())

# Find the angle MBC
angle_MBC = find_angle_MBC(AB_length, BC_length)
print(f"{angle_MBC}\u00B0")
