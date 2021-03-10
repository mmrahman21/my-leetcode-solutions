def isPalindrome(x: int) -> bool:
        
    number = str(x)
    if x < 0:
        return False
    l = len(number)
    mid = l // 2
    left = mid - 1
    print(left)
    
    if l % 2 == 0:
        right = mid
    else:
        right = mid + 1
        
    print(right)
        
    for i in range(left, -1, -1):
        print("Hello")
        if number[i] != number[right]:
            return False
        else:
            right += 1
            
    return True
    

print(isPalindrome(10))

