def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ('', '', False)

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string = "".join(merge_sort(list(first_string)))
    second_string = "".join(merge_sort(list(second_string)))

    if first_string == second_string:
        return (first_string, second_string, True)
    else:
        return (first_string, second_string, False)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_i, right_i = 0, 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1

    result.extend(left[left_i:])
    result.extend(right[right_i:])

    return result
