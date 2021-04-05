def myCoinChange(coins, amount):
    
    l = len(coins) 
    if l == 1:
        if amount % coins[0] == 0:
            return amount // coins[0]

        else:
            return -1
            
    if amount == coins[0]:
        return 1

    if amount == 0:
        return 0
  
    sol = [float('inf')]*(amount+1)
   

    sol[0] = 0

    for i in range(1, amount + 1):

        j = 0
        while j < l:
            if coins[j] <= i:
                sol[i] = min(sol[i], 1+sol[i-coins[j]])
            else:
               
                break

            j += 1
    
    if sol[amount]== inf:
        return -1
    else:
        return sol[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        return myCoinChange(coins, amount)
       
        
        
        
        