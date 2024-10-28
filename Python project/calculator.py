print("Hellow Guys!")

import math

def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    return area

def area_of_square():
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    return area

def area_of_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    return area

def area_of_triangle():
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    return area

def area_of_parallelogram():
    base = float(input("Enter the base length of the parallelogram: "))
    height = float(input("Enter the height of the parallelogram: "))
    area = base * height
    return area

def calculate_area():
    print("Choose a shape to find the area:")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Parallelogram")
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        print(f"The area of the circle is: {area_of_circle():.2f}")
    elif choice == '2':
        print(f"The area of the square is: {area_of_square():.2f}")
    elif choice == '3':
        print(f"The area of the rectangle is: {area_of_rectangle():.2f}")
    elif choice == '4':
        print(f"The area of the triangle is: {area_of_triangle():.2f}")
    elif choice == '5':
        print(f"The area of the parallelogram is: {area_of_parallelogram():.2f}")
    else:
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    calculate_area()
