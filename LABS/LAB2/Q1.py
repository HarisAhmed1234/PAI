def calculate_area_of_trapezoid(a, b, height):
    return ((a + b) / 2) * height

def calculate_area_of_parallelogram(base, height):
    return base * height

def calculate_surface_area_of_cylinder(radius, height):
    return 2 * 3.142 * radius * (radius + height)

def calculate_volume_of_cylinder(radius, height):
    return 3.142 * radius ** 2 * height

a = float(input("Enter the length of side a of the trapezoid: "))
b = float(input("Enter the length of side b of the trapezoid: "))
height_trapezoid = float(input("Enter the height of the trapezoid: "))

base_parallelogram = float(input("Enter the base of the parallelogram: "))
height_parallelogram = float(input("Enter the height of the parallelogram: "))

radius_cylinder = float(input("Enter the radius of the cylinder: "))
height_cylinder = float(input("Enter the height of the cylinder: "))

print(f"Area of the trapezoid: {calculate_area_of_trapezoid(a, b, height_trapezoid)}")
print(f"Area of the parallelogram: {calculate_area_of_parallelogram(base_parallelogram, height_parallelogram)}")
print(f"Surface area of the cylinder: {calculate_surface_area_of_cylinder(radius_cylinder, height_cylinder)}")
print(f"Volume of the cylinder: {calculate_volume_of_cylinder(radius_cylinder, height_cylinder)}")
