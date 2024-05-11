def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    positive_nums = [num for num in arr if num >= 0]
    negative_nums = [-num for num in arr if num < 0]

    if positive_nums:
        max_num = max(positive_nums)
        exp = 1
        while max_num // exp > 0:
            counting_sort(positive_nums, exp)
            exp *= 10

    if negative_nums:
        max_num = max(negative_nums)
        exp = 1
        while max_num // exp > 0:
            counting_sort(negative_nums, exp)
            exp *= 10

    negative_nums = [-num for num in reversed(negative_nums)]

    arr[:] = negative_nums + positive_nums


arr = [301, 52, 10, 6, 421, 102, 90, -1, -10, 0]
radix_sort(arr)
print("Arreglo ordenado:", arr)


