def insertion(arr):
    
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
            
        arr[j+1] = key
        
    return arr
        
arr = [8,1,5,7,2]
print(insertion(arr))