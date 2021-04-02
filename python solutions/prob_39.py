class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 1:
            if target < candidates[0]:
                return []
            elif target % candidates[0] == 0:
                return [[candidates[0] for _ in range(target // candidates[0])]]
            
            else:
                return []
        
        main_result = []
        
        candidates = sorted(candidates)
        
        i = 0
        while i < len(candidates):
            
            if candidates[i] == target:
                main_result.append([candidates[i]])
                return main_result
                
            elif candidates[i] > target:
                return main_result
            
            sol = []
            
            while sum(sol) <= target:
                
                if sum(sol) == target:
                    break
                    
                else:
                    sol.append(candidates[i])

                if sum(sol) == target:
                    main_result.append(sol)
                    break


                elif sum(sol) < target:
                    new_candidate = candidates[i+1:]
                    result = self.combinationSum(new_candidate, target-sum(sol))

                    if len(result) != 0:

                        for p in result:
                            partial_sol = sol[:]  # Copy without reference
                            partial_sol.extend(p)
                            main_result.append(partial_sol)
                           
                elif sum(sol) >= target:
                    break
                    
            i += 1

        return main_result
            
                
                
            
        
        
        