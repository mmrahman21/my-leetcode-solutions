class Solution:
    def merge(self, intervals):
        l = len(intervals)
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        result = []
        
        i = 1
        
        start = 0
        end = 0
        while i <= l - 1:
            if intervals[i][0] <= intervals[end][1]:
                if intervals[i][1] > intervals[end][1]:
                    end = i
                       
            else:
                result.append([intervals[start][0], intervals[end][1]])
                start = i
                end = i
            i = i+1
                
        if start <= l-1 and end <= l-1:
            result.append([intervals[start][0], intervals[end][1]])
        return result

print(Solution().merge([[1,4],[4,5]]))
        