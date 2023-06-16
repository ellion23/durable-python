def interpolation_search(array, target):
    (left, right) = (0, len(array) - 1)

    while array[right] != array[left] and array[left] <= target <= array[right]:
        index = left + (target - array[left]) * (right - left) // (array[right] - array[left])
        if target == array[index]:
            return index
        elif target < array[index]:
            right = index - 1
            print(left, right)
        else:
            left = index + 1
            print(left, right)
    if target == array[left]:
        return left
    return -1


def main():
    array = [1, 4, 5, 65, 123, 135, 201, 210, 211, 254, 265]
    print(array)
    print(interpolation_search(array, 211))


if __name__ == "__main__":
    main()
