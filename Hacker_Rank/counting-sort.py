# counting sort

def babyCountingSort(arr):
    counts = [0 for _ in range(max(arr)+1)]
    for num in arr:
        counts[num] += 1
    sorted = []
    for key, val in enumerate(counts):
        sorted.extend([key for _ in range(val)])
    return sorted
    
    
# input:
# 20
# 0 ab
# 6 cd
# 0 ef
# 6 gh
# 4 ij
# 0 ab
# 6 cd
# 0 ef
# 6 gh
# 0 ij
# 4 that
# 3 be
# 0 to
# 1 be
# 5 question
# 1 or
# 2 not
# 4 is
# 2 to{-truncated-}
def countSort(arr):
    counts = [[] for _ in range(len(arr)+1)]
    for i, num in enumerate(arr):
        counts[int(num[0])].append(num[1] if i >= len(arr)//2 else '-')
    sorted = []
    for key, bucket in enumerate(counts):
        sorted.extend(bucket)
    print(' '.join(sorted))
# output
# - - - - - to be or not to be - that is the question - - - -
        

if __name__ =="__main__":
    arr = """63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33"""
    
    arr = [int(x) for x in arr.split(' ')]
    print(arr)
    sorted = countingSort(arr)
    print(sorted)