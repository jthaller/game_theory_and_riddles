## 2. Distinct Pairs
-----
In this challenge, you will be given an array of integers and a target value. 
Determining the number of distinct pairs of elements in the array that sum to the target value.
Two pairs (a, b) and (c, d) are considered to be distinct if and only if the values in sorted order do not match, i.e., (1, 9) and (9, 1) are indistinct but (1, 9 ) and (9, 2) are distinct.

For instance given the array [1, 2, 3, 6, 7, 8, 9, 1] and a target value of 10, the seven pairs (1, 9), (2, 8), (3, 7), (8, 2), (9,1), and (1, 9) all sum to 10 and only three distinct pair: (1, 9), (2, 8), and (3, 7).

Function Description:
Complete the function numberOfPairs. The function must return an integer, the total number of distinct pairs of elements in the array that sum to the target value.

numberOfPairs has following parameters:
a[a[0], ..., an-1]]: an array of integers to select the pairs from 
k: target integer value to sum to

Constraints:  
- 1 <= n <= 500000
- 0 <= a[i] <= 1000000000
- 0 <= k <= 500000

		Sample Input 0:
		6
		1
		3
		46
		1
		3
		9
		47
		
		Sample Output 0:
		1
		
		Explanation 0:
		a = [1, 3, 46, 1, 3, 9], k = 47
		There are 4 pairs of unique elements where a[i]+a[j] = k
		1. (a[0] = 1, a[2] = 46)
		2. (a[2] = 46, a[0] = 1)
		3. (a[2] = 46, a[3] = 1)
		4. (a[3] = 1, a[2] = 46)