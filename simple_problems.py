# takes a numerical string, or int, and returns a string with
# added ','. e.g., 1000 = 1,000
def format_number(n):
    s = str(n) # cast argument to string
    r = '' # string to be returned at the end of function
    t = 0
    if n > 0:

        # for every char in String s starting from the end, add char to string r
        for i in range(len(str(s)) - 1, -1, -1):
            r = str(s)[i] + r
            t += 1
            if t == 3 and i > 0: # add ',' every 3 digits, skip if the beginning of String is reached
                r = ',' + r
                t = 0
    return r


# returns the count of passed parameters
def param_count(*args):
    return len(args)


# Determines if passed element n, exists in one or both given lists
# returns True if it only exists in one, otherwise returns False
def list_xor(n, list1, list2):
    i = 0
    for j in list1:
        if j == n:
            i += 1
            break
    for j in list2:
        if j == n:
            i += 1
            break

    return i == 1


# Takes a function as a string, and determines if it's valid,
# in which case returns True, otherwise returns False
def validate(s):
    paren = chr(40) + chr(41)
    l = {'def': 'missing def',
         ':': 'missing :',
         '(': 'missing paren',
         ')': 'missing paren',
         paren: 'missing param',
         '    ': 'missing indent',
         'validate': 'wrong name',
         'return': 'missing return'}

    for i in l:
        if i == paren and i in s:
            return 'missing param'
        if i not in s and i != paren:
            return l[i]
    return True


# custom zip function. Returns pairs of numbers from two
# given lists of equal length
def zap(a, b):
    return [(a[i], b[i]) for i in range(0, len(a))]


# print(format_number(100000000))

# print(param_count(60,'6'))

# print(list_xor(2, (3, 4, 5), (3, 4, 5)))

# print(validate("def validate(s): return s"))

print(zap([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]))
