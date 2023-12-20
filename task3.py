# Задание 3
# На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам)
# отсортирует данный ей массив чисел. Массив может быть любого размера со случайным
# порядком чисел (в том числе и отсортированным). Объяснить, почему вы считаете, что функция
# соответствует заданным критериям.

# Сортировка слиянием

def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def printList(array):
    for item in array:
        print(item, end=" ")


if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    print("Изначальный массив:")
    printList(array)

    mergeSort(array)

    print("Отсортированный массив:")
    printList(array)

# Сложность представленного алгоритма O(n log n), что является одним из лучших показателей среди алгоритмов сортировки.