def sort(array):
    length = len(array)
    max_item_length = get_max_len(array)
    lists = [[] for i in range(max_item_length)]
    for i in range(max_item_length):
        keys = []
        for j in range(len(array)):
            keys.append((array[j], key_for_index(array[j], i), j))
        # print(keys)
        temp = sorted(keys, key=lambda x: x[1])
        # print(temp)
        new_array = array
        for j in range(len(temp)):
            if temp[j][1] != -1:
                new_array[j] = temp[j][0]

        array = new_array
        print(array, len(array))
        # for a, b, c in temp:
        #     print(a, end=" ")
        # print()



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


def main():
    array = [str(i) for i in [4, 5, 1, 123, 201, 210, 211, 265, 254, 135, 65]]
    print("Unsorted array: ", end="")
    print(*array)

    array = sort(array)

    # print("Sorted array: ", end="")
    # print(*array)


if __name__ == "__main__":
    main()
