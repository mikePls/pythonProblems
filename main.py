
#Objective: Create a function that returns all pairs whose sum equals a given target from an array of integers
def sum_of_two(arr=[], target=None):
    for i in arr:
        if target-i in arr:
            print(f'{i} + {target-i} = {target}')


def sum_of_two_v2(arr, target):
    if arr is None:
        arr = []
    l_pointer = 0
    r_pointer = len(arr)-1

    while l_pointer < r_pointer:
        if arr[l_pointer] + arr[r_pointer] == target:
            print(f'{arr[l_pointer]} + {arr[r_pointer]} = {target}')
            l_pointer +=1
        elif arr[l_pointer] + arr[r_pointer] < target:
            l_pointer +=1
        else:
            r_pointer -=1




arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*arr, sep=',')
sum_of_two_v2(arr, 10)

