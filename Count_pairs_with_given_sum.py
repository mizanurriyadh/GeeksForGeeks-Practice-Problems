def pairsCount(arr, n, sum):
    count = 0
    
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == sum:
                count += 1
    
    return count
    

arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is : ", pairsCount(arr, n, sum))


# Output : Count of pairs is 3
# Source : https://www.geeksforgeeks.org/count-pairs-with-given-sum/
