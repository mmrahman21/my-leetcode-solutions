class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_time_in_mins = int(current[:2])*60 + int(current[3:])
        correct_time_in_mins = int(correct[:2])*60 + int(correct[3:])
        
        correct_minus_current = correct_time_in_mins - current_time_in_mins
        
        min_operations = 0
        
        for increment in [60, 15, 5, 1]:
            min_operations += (correct_minus_current // increment)
            correct_minus_current = correct_minus_current % increment
            
            if correct_minus_current == 0:
                break
            
        return min_operations