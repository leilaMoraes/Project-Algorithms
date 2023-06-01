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
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result.extend(left[l:])
    result.extend(right[r:])

    return result

