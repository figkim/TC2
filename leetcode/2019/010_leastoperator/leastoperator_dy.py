class Solution:
    def findInitial(self, x, target):
        if len(self.square) == 0:
            value = 1
            for i in range(32):
                self.square.append(value)
                if value > target:
                    break
                value *= x
        
        for i, num in enumerate(self.square):
            if num >= target:
                return i, num
    
            
    def findTarget(self, x, target):
        if target in self.memo:
            return self.memo[target]
        if target == 1:
            return 1
        if target == x:
            return 0
        
        count, value = self.findInitial(x, target)
        
        assert count > 0 
        if value == target:
            self.memo[target] = abs(count-1)
        else:
            if value - target < target:
                self.memo[target] = self.findTarget(x, value-target) + count
            
            value = int(value/x)
            candidate = self.findTarget(x, target-value) + abs(count-2) + 1
            if target not in self.memo or self.memo[target] > candidate:
                self.memo[target] = candidate
        return self.memo[target]
    
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        self.memo = {}
        self.square = []
        value = 1

        return self.findTarget(x, target)
