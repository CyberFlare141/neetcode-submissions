class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                width = j - i
                current_height = min(heights[i], heights[j])
                current_area = width * current_height
                
                if current_area > answer:
                    answer = current_area
                    
        return answer