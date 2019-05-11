# Reverse Array or String in Iterative Way
# Source -  https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
# Pseudocode - WHILE(START<END)
#              {
#                    TEMP = Array[START]
#                    Array[Start] = Array[END]
#                    Array[END] = Array[TEMP]
#                    START++
#                    END++
#              }


def reverseArray(Array, start, end):
    while start < end:
        Array[start], Array[end] = Array[end], Array[start]
        start += 1
        end -= 1


def PrintArray(Array):
    print(Array)
    print('')


def Main():
    Array = list(map(int, input().split()))
    ArraySize = len(Array)
    print("Before Reverse: ")
    PrintArray(Array)
    reverseArray(Array, 0, ArraySize - 1)
    print("After Reverse: ")
    PrintArray(Array)


if __name__ == '__main__':
    Main()