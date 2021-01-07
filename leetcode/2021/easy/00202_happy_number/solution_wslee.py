class Solution:
    def isHappy(self, n: int) -> bool:

        num_set = set()
        while n != 0 and n not in num_set:
            num_set.add(n)
            tmp_sum = 0
            str_n = str(n)
            for i in range(len(str_n)):
                tmp_sum += int(str_n[i]) ** 2
            n = tmp_sum

            print(n)

        if n == 1:
            return True
        return False

