class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        l = 0    #row
        r = (m*n) - 1  #column

        while l <= r:
           
           mid = (l+r) // 2

           row = mid // n
           col = mid % n 

           mid_val = matrix[row][col]

           if mid_val == target:
              return True
            
           elif mid_val < target:
                l = mid + 1
            
           else :
                r = mid -1

        return False