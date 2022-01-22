import logging
import math


def get_line_distance(x_axis1, x_axis2, y_axis1, y_axis2):
    return math.sqrt((x_axis2 - x_axis1) * (x_axis2 - x_axis1) + (y_axis2 - y_axis1) * (y_axis2 - y_axis1))


def user_input():
    try:
        x1 = int(input("Enter x1 value"))
        x2 = int(input("Enter x2 value"))
        y1 = int(input("Enter y1 value"))
        y2 = int(input("Enter y2 value"))

    except Exception:
        logging.exception("input error")

    return get_line_distance(x1, x2, y1, y2)


def compare_line(line_length1, line_length2):
    if line_length1 > line_length2:
        return line_length1
    else:
        return line_length2


if __name__ == "__main__":
    print("Enter first line")
    line_length1 = user_input()
    print("Enter second line")
    line_length2 = user_input()
    print(line_length1, "compare", line_length2, "greater length is", compare_line(line_length1, line_length2))

