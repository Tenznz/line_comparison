import logging
import math


class LineCompare:
    def __init__(self):
        pass

    def get_line_distance(self, x_axis1, x_axis2, y_axis1, y_axis2):
        """

        :param x_axis1:
        :param x_axis2:
        :param y_axis1:
        :param y_axis2:
        :return: length
        """
        return math.sqrt((x_axis2 - x_axis1) * (x_axis2 - x_axis1) + (y_axis2 - y_axis1) * (y_axis2 - y_axis1))

    def user_input(self):
        """
        taking input from user
        :return:  distance
        """
        try:
            x1 = int(input("Enter x1 value"))
            x2 = int(input("Enter x2 value"))
            y1 = int(input("Enter y1 value"))
            y2 = int(input("Enter y2 value"))

        except Exception:
            logging.exception("input error")

        return self.get_line_distance(x1, x2, y1, y2)

    def compare_line(self, line_length1, line_length2):
        """
        compare the two line
        :param line_length1:
        :param line_length2:
        :return: greater length will return
        """
        if line_length1 > line_length2:
            return line_length1
        else:
            return line_length2


if __name__ == "__main__":
    line_compare = LineCompare()
    print("Enter first line")
    line_length1 = line_compare.user_input()
    print("Enter second line")
    line_length2 = line_compare.user_input()
    print(line_length1, "compare", line_length2, "greater length is",
          line_compare.compare_line(line_length1, line_length2))
