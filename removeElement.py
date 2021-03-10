def removeElement(nums, val):
        to_be_filled_index = 0
        
        length = len(nums)
        
        for i in range(length):
            if nums[i] ! = val:
                nums[to_be_filled_index] = nums[i]
                to_be_filled_index += 1
                
        return to_be_filled_index
    

print(removeElement([0,1,2,2,3,0,4,2], 2))