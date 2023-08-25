from math import sqrt


def the_longest_line(l1x1, l1y1, l1x2, l1y2, l2x1, l2y1, l2x2, l2y2):
    l1x1 = int(l1x1)
    l1y1 = int(l1y1)
    l1x2 = int(l1x2)
    l1y2 = int(l1y2)
    l2x1 = int(l2x1)
    l2y1 = int(l2y1)
    l2x2 = int(l2x2)
    l2y2 = int(l2y2)
    first_line_first_point = l1x1, l1y1
    first_line_second_point = l1x2, l1y2
    second_line_first_point = l2x1, l2y1
    second_line_second_point = l2x2, l2y2
    length_line_1 = sqrt((l1x2 - l1x1) ** 2 + (l1y2 - l1y1) ** 2)
    length_line_2 = sqrt((l2x2 - l2x1) ** 2 + (l2y2 - l2y1) ** 2)
    coordinates_first_line_first_point = abs(l1x1) + abs(l1y1)
    coordinates_first_line_second_point = abs(l1x2) + abs(l1y2)
    coordinates_second_line_first_point = abs(l2x1) + abs(l2y1)
    coordinates_second_line_second_point = abs(l2x2) + abs(l2y2)
    if length_line_1 >= length_line_2:
        if coordinates_first_line_first_point <= coordinates_first_line_second_point:
            return f'{first_line_first_point}{first_line_second_point}'
        return f'{first_line_second_point}{first_line_first_point}'
    else:
        if coordinates_second_line_first_point <= coordinates_second_line_second_point:
            return f'{second_line_first_point}{second_line_second_point}'
        return f'{second_line_second_point}{second_line_first_point}'


first_l_first_x = float(input())
first_l_first_y = float(input())
first_l_second_x = float(input())
first_l_second_y = float(input())
second_l_first_x = float(input())
second_l_first_y = float(input())
second_l_second_x = float(input())
second_l_second_y = float(input())
print(the_longest_line(first_l_first_x, first_l_first_y, first_l_second_x, first_l_second_y,
                       second_l_first_x, second_l_first_y, second_l_second_x, second_l_second_y))
