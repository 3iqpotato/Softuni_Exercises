def get_magic_triangle(n):
    my_triangle = []

    for idx in range(1, n+1):
        list_line = [1]*idx

        if len(list_line) > 2:
            mat_prev_list = my_triangle[-1]

            for i in range(1, len(list_line) - 1):
                list_line[i] = mat_prev_list[i-1] + mat_prev_list[i]

        my_triangle.append(list_line)

    return my_triangle





print(get_magic_triangle(5))