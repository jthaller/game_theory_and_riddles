# remove values in a list < 10 in place.
# Time complexity O(n)
# Space complexity O(1)

list1 = [1,2,7,4,13,6,7,8,20,10,11,12,14,14,15]

def remove_vals(l):
    i=0
    for j in range(len(list1)):
        if l[j] >= 10: #i.e. yes remove
            l[i] = l[j]
            i += 1
    return l[:i]

l2 = remove_vals(list1)
print(l2)


