def sel_1(arr):
    n=len(arr)
    for i in range(n):
        min_index=1
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
arr=[64,25,12,22,11]
sel_1(arr)
print('选择排序',arr)