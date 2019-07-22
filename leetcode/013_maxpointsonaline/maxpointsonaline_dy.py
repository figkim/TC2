
inf = 9999.9
class Solution:
    def getLine(self, x, y):
        if x[0] == y[0]:
            a = inf
            b = x[0]
        elif x[1] == y[1]:
            a = x[1]
            b = inf 
        else:
            a = float((x[1]-y[1])/(x[0]-y[0]))
            b = round(float(x[1] - a * x[0]),4)
        return [a, b]
    
    def onLine(self, line, x):
        if line[0] == inf:
            return x[0] == line[1]
        elif line[1] == inf:
            return x[1] == line[0]
        return round(line[0] * x[0] + line[1] - x[1],4) == 0
    
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1 
        lines = {}
        for i in range(len(points)-1):
            x = points[i]
            for j in range(i+1, len(points)):
                y = points[j]
                new_line = self.getLine(x, y)
                already_exists = False
                for key in lines:
                    line = lines[key][0]
                    if line[0] == new_line[0] and line[1] == new_line[1]:
                        already_exists = True
                if not already_exists:
                    lines[len(lines)] = [new_line, 0]
        ans = 0
        
        
        for key in lines:
            for point in points:
                if self.onLine(lines[key][0], point):
                    lines[key][1] += 1
            if lines[key][1] > ans:
                ans = lines[key][1]
        return ans 
                        
            
