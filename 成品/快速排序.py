def quick_1(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        less=[x for x in arr[1:]if x<=pivot]
        greater=[x for x in arr[1:]if x>pivot]
        return quick_1(less)+[pivot]+quick_1(greater)
arr=[55,25,13,23,13]
sorted_arr=quick_1(arr)
print("快速排序",sorted_arr)
