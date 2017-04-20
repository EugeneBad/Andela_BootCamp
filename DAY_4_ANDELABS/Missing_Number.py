def find_missing(list_1, list_2):
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    if len(sorted_list_1) == len(sorted_list_2):
        return 0

    try:
        for index in range(len(sorted_list_1)):
            if sorted_list_1[index] != sorted_list_2[index]:
                return sorted_list_2[index]

            if index == len(sorted_list_1) - 1:
                return sorted_list_2[-1]
    except IndexError:
        return sorted_list_1[-1]


