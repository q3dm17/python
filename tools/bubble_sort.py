def strange_bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                list[i], list[j] = list[j], list[i]
                print(list)


def bubble_sort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j+1], list[j] = list[j], list[j+1]
                print(list)
                swapped = True
        if not swapped:
            return


l = [4, 7, 2, 9]
# bubble_sort(l)
l = [8, 7, 9, 3, 5]
print (l)
strange_bubble_sort(l)
print("".center(80,"-"))
l = [8, 7, 9, 3, 5]
bubble_sort(l)