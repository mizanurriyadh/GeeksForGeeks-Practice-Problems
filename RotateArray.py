# Problem Link - https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0

def Rotation(array, D):
    array = array[D:] + array[:D]
    return array


def Print(array):
    for i in array:
        print(i, end=" ")
    print()


def main():
    T = int(input())
    while (T):
        T -= 1
        N, D = list(map(int, input().split()))
        array = list(map(int, input().split()))
        new_array = Rotation(array, D)
        Print(new_array)


if __name__ == '__main__':
    main()
