import math

class GeometricCalculator:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius**2

    @staticmethod
    def circle_perimeter(radius):
        return 2 * math.pi * radius

    @staticmethod
    def rectangle_area(length, width):
        return length * width

    @staticmethod
    def rectangle_perimeter(length, width):
        return 2 * (length + width)

    @staticmethod
    def triangle_area(base, height):
        return 0.5 * base * height

    @staticmethod
    def triangle_perimeter(side1, side2, side3):
        return side1 + side2 + side3

    @staticmethod
    def square_area(side_length):
        return side_length ** 2

    @staticmethod
    def square_perimeter(side_length):
        return 4 * side_length

    @staticmethod
    def cube_surface_area(side_length):
        return 6 * side_length ** 2

    @staticmethod
    def cube_volume(side_length):
        return side_length ** 3

    @staticmethod
    def sphere_surface_area(radius):
        return 4 * math.pi * radius ** 2

    @staticmethod
    def sphere_volume(radius):
        return (4 / 3) * math.pi * radius ** 3

    @staticmethod
    def cylinder_surface_area(radius, height):
        return 2 * math.pi * radius * (radius + height)

    @staticmethod
    def cylinder_volume(radius, height):
        return math.pi * radius ** 2 * height

    @staticmethod
    def cone_surface_area(radius, height):
        base_area = math.pi * radius ** 2
        side_area = math.pi * radius * math.sqrt(radius ** 2 + height ** 2)
        return base_area + side_area

    @staticmethod
    def cone_volume(radius, height):
        return (1 / 3) * math.pi * radius ** 2 * height

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    calculator = GeometricCalculator()

    while True:
        print("\nChoose a shape:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Square")
        print("5. Cube")
        print("6. Sphere")
        print("7. Cylinder")
        print("8. Cone")
        print("9. Exit")
        choice = input("Enter the number corresponding to the shape: ")

        if choice == '1':
            radius = get_float_input("Enter the radius of the circle: ")
            print("Area of the circle:", calculator.circle_area(radius))
            print("Perimeter of the circle:", calculator.circle_perimeter(radius))
        elif choice == '2':
            length = get_float_input("Enter the length of the rectangle: ")
            width = get_float_input("Enter the width of the rectangle: ")
            print("Area of the rectangle:", calculator.rectangle_area(length, width))
            print("Perimeter of the rectangle:", calculator.rectangle_perimeter(length, width))
        elif choice == '3':
            base = get_float_input("Enter the base length of the triangle: ")
            height = get_float_input("Enter the height of the triangle: ")
            print("Area of the triangle:", calculator.triangle_area(base, height))
            side1 = get_float_input("Enter the length of the first side of the triangle: ")
            side2 = get_float_input("Enter the length of the second side of the triangle: ")
            side3 = get_float_input("Enter the length of the third side of the triangle: ")
            print("Perimeter of the triangle:", calculator.triangle_perimeter(side1, side2, side3))
        elif choice == '4':
            side_length = get_float_input("Enter the length of the side of the square: ")
            print("Area of the square:", calculator.square_area(side_length))
            print("Perimeter of the square:", calculator.square_perimeter(side_length))
        elif choice == '5':
            side_length = get_float_input("Enter the length of the side of the cube: ")
            print("Surface area of the cube:", calculator.cube_surface_area(side_length))
            print("Volume of the cube:", calculator.cube_volume(side_length))
        elif choice == '6':
            radius = get_float_input("Enter the radius of the sphere: ")
            print("Surface area of the sphere:", calculator.sphere_surface_area(radius))
            print("Volume of the sphere:", calculator.sphere_volume(radius))
        elif choice == '7':
            radius = get_float_input("Enter the radius of the cylinder: ")
            height = get_float_input("Enter the height of the cylinder: ")
            print("Surface area of the cylinder:", calculator.cylinder_surface_area(radius, height))
            print("Volume of the cylinder:", calculator.cylinder_volume(radius, height))
        elif choice == '8':
            radius = get_float_input("Enter the radius of the cone: ")
            height = get_float_input("Enter the height of the cone: ")
            print("Surface area of the cone:", calculator.cone_surface_area(radius, height))
            print("Volume of the cone:", calculator.cone_volume(radius, height))
        elif choice == '9':
            break
        else:
            print("Invalid choice. Enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
