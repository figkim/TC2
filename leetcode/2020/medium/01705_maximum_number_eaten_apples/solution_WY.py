class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        
        die = [0 for _ in range(len(apples) + max(days))]
        current = 0
        count = 0
        deadline = 0
        
        for i,apple in enumerate(apples):
            #current -= die[i]
            #current = max(0,current)
            current += apple
            die[i+days[i]] += apple
            deadline = max(deadline,days[i])
            if current > 0 and deadline > 0:
                count += 1
                current -= 1
                deadline -= 1

        for i in range(len(apples), len(apples) + max(days)):
            #current -= die[i]
            #current = max(0,current)
            if current > 0 and deadline > 0:
                count += 1
                current -= 1
                deadline -= 1
            else:
                return count

            
            