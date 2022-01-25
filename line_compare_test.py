from line_comparison.line_compare import LineCompare


def test_get_line_distance():
    """
    test get_line_distance(x1,x2,y1,y2)
    :return:
    """
    line_compare_obj = LineCompare()
    assert line_compare_obj.get_line_distance(0, 0, 1, 3) == 2


def test_compare_line():
    """
    test compare_line(len1,len2)
    :return:
    """
    line_compare_obj = LineCompare()
    assert line_compare_obj.compare_line(2, 4) == 4
