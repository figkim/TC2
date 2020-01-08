class Solution:
    def countAndSay(self, n: int) -> str:
        x = 1
        if n > 1:
            for i in range(n-1):
                new_x = 0
                values = str(x)
                lastValue = 0
                valueCount = 0
                for char in values:
                    value = int(char)
                    if lastValue != value:
                        new_x *= 100
                        new_x += 10 * valueCount + lastValue
                        lastValue = value
                        valueCount = 1
                    else:
                        valueCount += 1
                new_x *= 100
                new_x += 10 * valueCount + lastValue
                x = new_x
        return str(x)
