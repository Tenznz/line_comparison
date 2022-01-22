import math


def get_line_distance(x_axis1, x_axis2, y_axis1, y_axis2):
    line = math.sqrt((x_axis2 - x_axis1) * (x_axis2 - x_axis1) + (y_axis2 - y_axis1) * (y_axis2 - y_axis1))
    print("distance-between (", x_axis1, ",", y_axis1, "),", "(", x_axis2, ",", y_axis2, ") is ", line)


if __name__ == "__main__":
    x1 = int(input("Enter x1 value"))
    x2 = int(input("Enter x2 value"))
    y1 = int(input("Enter y1 value"))
    y2 = int(input("Enter y2 value"))
    get_line_distance(x1, x2, y1, y2)
