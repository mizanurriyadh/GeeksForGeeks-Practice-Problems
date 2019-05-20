# Problem Source - https://practice.geeksforgeeks.org/problems/searching-a-number/0

def search(arr, n, x):
    for i in range(0, n):
        if(arr[i] == x):
            return i
    return -1


def Main():
    t = int(input())
    while(t):
        t -= 1
        n, x = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        result = search(arr, n, x)
        if (result == -1):
            print("-1")
        else:
            print(result+1)


if __name__  == '__main__':
    Main()