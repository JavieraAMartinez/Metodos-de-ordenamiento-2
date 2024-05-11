
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

print("Ingrese los números que desea ordenar, separados por espacios:")
user_input = input()
numbers = list(map(int, user_input.split()))

print("Números ingresados:", numbers)
sorted_numbers = shell_sort(numbers)
print("Números ordenados:", sorted_numbers)
