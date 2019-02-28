def merge_sort(arr):
    print(arr)

    def merge(arr, left_bound, middle, right_bound):
        lefts = arr[left_bound:middle+1]
        lefts.append(float("inf"))
        rights = arr[middle+1:right_bound + 1]
        rights.append(float("inf"))
        left_cur = 0
        right_cur = 0
        for k in range(left_bound, right_bound + 1):
            if lefts[left_cur] <= rights[right_cur]:
                arr[k] = lefts[left_cur]
                left_cur += 1
            else:
                arr[k] = rights[right_cur]
                right_cur += 1

    def merge_req(arr, left, right):
        if left < right:
            middle = (left + right) // 2
            merge_req(arr, left, middle)
            merge_req(arr, middle + 1, right)
            merge(arr, left, middle, right)

    merge_req(arr, 0, len(arr)-1)
    print(arr)


merge_sort(list(range(8, 0, -1)))
merge_sort([3,2,7,1,5])
