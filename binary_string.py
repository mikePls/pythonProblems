# Problem: Generate all binary strings with n bits

# solution:

def append_at_front(x, N):
    return [x for element in N]


def bit_strings(n):
    if n == 0: return []
    if n == 1: return ['0', '1']
    else:
        return (append_at_front('0', bit_strings(n - 1)) + append_at_front('1', bit_strings(n - 1)))


def rangeToList(k):
    result = []
    for i in range(0,k):
        result.append(str(i))
        return result

def baseKStrings(n,k):
    if n == 0 : return n
    if n == 1: return rangeToList(k)
    return [digit+bitstring for digit in baseKStrings(1 ,k)
    for bitstring in baseKStrings(n-1,k)]




print(bit_strings(10))
