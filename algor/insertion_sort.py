from itertools import count

def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i+1] = key
        print(array)


def main():
    insertion_sort([3, 7, 33, 2, 6, 0])
    for key,j in zip([3, 7, 33, 2, 6, 0][1:], count()):
        print(key,j)


if __name__ == '__main__':
    main()