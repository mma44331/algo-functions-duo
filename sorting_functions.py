

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range((n-i-1)):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([5,9,4,6,2]))
