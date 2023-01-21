# User function Template for python3

class Solution:
    def select(self, arr, i):
        # code here
        selectionSort(arr)
        print(arr)

    def selectionSort(self, arr, n):
        # code here
        for i in range(0, len(arr)-1):
            curr_min = i

            for j in range(i+1, len(arr)):
                if arr[j] < arr[curr_min]:
                    curr_min = j

            arr[i], arr[curr_min] = arr[curr_min], arr[i]


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends
