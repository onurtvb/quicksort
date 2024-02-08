arr = [10,5,6,1,2,12,5,7]


def partition(low: int, high: int):
    pivot = arr[high]
    i = low - 1

    for x in range(low, high):
        if arr[x] < pivot:
            i+=1
            (arr[i], arr[x]) = (arr[x],arr[i])
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])

    return i+1



def quicksort(low: int, high: int):
    if low < high:
        part = partition(low,high)
        quicksort(low, part-1)
        quicksort(part+1, high)

def main():
    print('Original array:',arr)
    quicksort(0,len(arr)-1)
    print('Sorted array:',arr)



if __name__ == '__main__':
    main()