# quicksort
# part one https://www.hackerrank.com/challenges/quicksort1/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def quickSort(arr):
    pivot = arr[0]
    left = set()
    equal=set()
    equal.add(pivot)
    right=set()
    for num in arr:
        if num < pivot:
            left.add(num)
        elif num == pivot:
            equal.add(num)
        else:
            right.add(num)
    left = list(left)
    left.extend(equal)
    left.extend(right)
    return left

if __name__ == '__main__':
    arr = [int(x) for x in '4 9 5 3 7 1 2'.split(' ')]
    sorted = quickSort(arr)
    print(arr)
    print(sorted)
