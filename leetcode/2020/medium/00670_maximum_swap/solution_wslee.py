class Solution:
    def maximumSwap(self, num: int) -> int:

        str_num_list = list(str(num))
        res = str_num_list[:]

        for i in range(len(res) - 1):
            for j in range(i + 1, len(res)):
                str_num_list[i], str_num_list[j] = str_num_list[j], str_num_list[i]
                if str_num_list > res:
                    res = str_num_list[:]
                str_num_list[i], str_num_list[j] = str_num_list[j], str_num_list[i]

        return int("".join(res))
