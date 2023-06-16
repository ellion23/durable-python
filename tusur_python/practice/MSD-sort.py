def key_for_index(item, n):
    if n < len(item):
        return ord(item[n])
    return -1


def get_max_len(array):
    max_len = 0
    for item in array:
        if len(item) > max_len:
            max_len = len(item)
    return max_len


def find_min_max(array, n):
    min_element = key_for_index(array[0], n)
    max_element = min_element
    for item in array:
        current_key = key_for_index(item, n)
        if min_element > current_key:
            min_element = current_key
        if max_element < current_key:
            max_element = current_key
    return [min_element, max_element]


def count_sort(array, start, end, n, max_len):
    if n > max_len:
        return
    min_max = find_min_max(array[start:end + 1], n)
    if min_max[0] == min_max[1]:
        if min_max[0] == -1:
            return
        count_sort(array, start, end, n + 1, max_len)
        return
    min_key = min_max[0]
    max_key = min_max[1]
    support_size = max_key - min_key + 1
    support = [0 for i in range(support_size)]
    for item in array[start:end + 1]:
        support[key_for_index(item, n) - min_key] += 1
    sort_size = end - start + 1
    for i in range(len(support) - 1, -1, -1):
        sort_size -= support[i]
        support[i] = sort_size
    result = [None for i in range(len(array[start:end + 1]))]
    for item in array[start:end + 1]:
        result[support[key_for_index(item, n) - min_key]] = item
        support[key_for_index(item, n) - min_key] += 1
    array[start:end + 1] = result

    start_index = 0
    for i in support:
        if i != start_index:
            count_sort(array, start_index + start, start + i - 1, n + 1, max_len)
            start_index = i


def msd_sort(array):
    max_len = get_max_len(array)
    count_sort(array, 0, len(array) - 1, 0, max_len)


if __name__ == '__main__':
    array = [str(i) for i in [4, 5, 1, 123, 201, 210, 211, 265, 254, 135, 65]]
    print("Unsorted array: ", end="")
    print(*array)

    msd_sort(array)
    # 1 123 135 201 210 211 254 265 4 5 65
    # 1 123 135 201 210 211 265 254 4 5 65
    print("Sorted array: ", end="")
    print(*array)
