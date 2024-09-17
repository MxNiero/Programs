def find_uniq(arr):
    for n in arr:
        if arr.count(n) == 1:
            return n


find_uniq([ 10, 1, 1, 2, 1, 1 ])