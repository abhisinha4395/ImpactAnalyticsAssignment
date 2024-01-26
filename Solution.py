class Solution:
    def graduate(self, days):
        
        def backtrack(n, ways):
            nonlocal miss
            if n == 0:
                if any(ways[-4:]):
                    if ways[-1] == 0:
                        miss += 1
                    return 1
                else:
                    return 0
            
            if not any(ways[-4:]) and len(ways) >= 4:
                return 0
        
            count = 0
            for i in [0, 1]:
                ways.append(i)
                count += backtrack(n-1, ways)
                ways.pop()
             
            return count
        
        miss = 0
        return backtrack(days, []), miss

days = int(input("Enter the graduation day : "))
ways, miss = Solution().graduate(days)
print("{}/{}".format(miss, ways))
