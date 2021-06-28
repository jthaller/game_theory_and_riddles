from itertools import combinations, permutations
# permutations considers each elument as unique
# combinations considers only unique elements in the list,
# but it will give you (1, 2) and (2, 1)

def distinct_pairs(a, target):
    pairs = [items for items in combinations(a, r=2)]
    num_pairs = 0
    for tup in pairs:
        if tup[0] + tup[1] == target:
            num_pairs += 1
            print(tup)
    # print(num_pairs)
    print(num_pairs)
    return num_pairs

def distinct_pairs2(a, target):
    num_pairs = 0
    no_duplicates_set = set(a) # O(n)
    no_duplicates = list(no_duplicates_set) # O(n)
    for num in a: #O(n)
        if target - a in no_duplicates_set: # O(1)
            num_pairs += 1 #O(n)
    
    
    
        
# this solution doesn't work
def numberOfPairs(a, k):
    history = {}
    result = set()
    for num in a:
        if num in history:
            result.add(tuple(sorted([num, history[num]])))
        else:
            history[num] = k - num
    print(history)
    print(result)
    return len(result)


if __name__ == "__main__":
    a = [1, 2, 3, 6, 7, 8, 9, 1] 
    b = [1, 3, 46, 1, 3, 9]
    distinct_pairs(a, 10)
    print(numberOfPairs(a, 10))
