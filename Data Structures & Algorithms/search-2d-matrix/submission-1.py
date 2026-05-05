class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      r=len(matrix)
      c=len(matrix[0])
      for i in range(r):
        print(i,matrix[i][c-1])
        if matrix[i][c-1]>=target:
            break
      l=0
      rr=c-1
      
      while l<=rr:
        mid=(l+rr)//2
        if target==matrix[i][mid]:
            return True
        elif target>matrix[i][mid]:
            l=mid+1
        else:
            rr=mid-1
        
        

      print(r,c)

            

      return False