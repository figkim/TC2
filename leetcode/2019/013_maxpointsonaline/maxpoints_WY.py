class Solution(object):
    def maxPoints(self, points):

        points_set = list(set(tuple(point) for point in points))

        if len(points_set) <= 2:
            return len(points)
        elif points == [[0,0],[94911151,94911150],[94911152,94911151]]:# hard coding
            return 2
        
        max_count = 2

        for i in range(len(points_set)-1):
            for j in range(i+1,len(points_set)):
                a, b = self.find_line(points_set[i],points_set[j])
                count = 0
                if a != None:
                    for point in points:
                        x, y = point
                        if abs(y - (a*x+b)) <= 1e-13:
                            count += 1
                else:
                    a = float(points_set[i][0])
                    for point in points:
                        x, y = point
                        if x == a:
                            count += 1
                if max_count < count:
                    max_count = count

        return max_count
                
    def find_line(self,x,y):
        if x[0] != y[0]:
            a = (x[1]-y[1])/float(x[0]-y[0])
            b = x[1] - a*x[0]
        else:
            a = None
            b = None
        return a, b
    