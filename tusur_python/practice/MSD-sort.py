def key_for_index(text, n):
    if n < len(text):
        return ord(text[n])
    return -1


def get_max_len(list_text):
    max_len = 0
    for text in list_text:
        if len(text) > max_len:
            max_len = len(text)
    return max_len


def find_min_max(list_text, n):
    min_element = key_for_index(list_text[0], n)
    max_element = min_element
    for text in list_text:
        current_key = key_for_index(text, n)
        if min_element > current_key:
            min_element = current_key
        if max_element < current_key:
            max_element = current_key
    return [min_element, max_element]


def count_sort(text_list, start, end, n, max_len):
    if n > max_len:
        return
    min_max = find_min_max(text_list[start:end + 1], n)
    if min_max[0] == min_max[1]:
        if min_max[0] == -1:
            return
        count_sort(text_list, start, end, n + 1, max_len)
        return
    min_key = min_max[0]
    max_key = min_max[1]
    support_size = max_key - min_key + 1
    support = [0 for i in range(support_size)]
    for text in text_list[start:end + 1]:
        support[key_for_index(text, n) - min_key] += 1
    sort_size = end - start + 1
    for i in range(len(support) - 1, -1, -1):
        sort_size -= support[i]
        support[i] = sort_size
    result = [None for i in range(len(text_list[start:end + 1]))]
    for text in text_list[start:end + 1]:
        result[support[key_for_index(text, n) - min_key]] = text
        support[key_for_index(text, n) - min_key] += 1
    text_list[start:end + 1] = result

    start_index = 0
    for i in support:
        if i != start_index:
            count_sort(text_list, start_index + start, start + i - 1, n + 1, max_len)
            start_index = i


def msd_sort(text_list):
    max_len = get_max_len(text_list)
    count_sort(text_list, 0, len(text_list) - 1, 0, max_len)


if __name__ == '__main__':
    arr = [4, 5, 1, 123, 201, 210, 211, 221, 254, 135]
    arr = [str(i) for i in arr]
    print("Unsorted array: ", end="")
    print(*arr)

    msd_sort(arr)

    print("Sorted array: ", end="")
    print(*arr)
