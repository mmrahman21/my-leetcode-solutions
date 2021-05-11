class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = len(intervals)
        if l == 0:
            return [newInterval]
        
        res = []
        
        i = 0
        
        while intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            if i >= l:
                break
        if i < l:
            start = min(intervals[i][0], newInterval[0])
            print(start)

            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])

            elif intervals[i][1] > newInterval[1]:
                res.append([start, intervals[i][1]])
                res.extend(intervals[i+1:])
            else:
                flag = 0
                while newInterval[1] >= intervals[i][0]:
                    if newInterval[1] <= intervals[i][1]:
                        res.append([start, intervals[i][1]])
                        flag = 1

                    i += 1
                    if i >= l:
                        break

                if not flag:
                    res.append([start, newInterval[1]])
                if i < l:
                    res.extend(intervals[i:])
        else:
            res.append(newInterval)
        print(res)
        
        return res
                
        