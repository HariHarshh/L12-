def square_perimeter(side):
    return 4 * side



def rectangle_perimeter(length, width):
    return 2 * (length + width)


side_length = 5
rect_length = 10
rect_width = 4

print("Square perimeter:", square_perimeter(side_length))
print("Rectangle perimeter:", rectangle_perimeter(rect_length, rect_width))