def find_max_min(elements):
    sorted_elements = sorted(elements)

    if sorted_elements[0] == sorted_elements[-1]:
        return [len(sorted_elements)]

    return [sorted_elements[0], sorted_elements[-1]]
