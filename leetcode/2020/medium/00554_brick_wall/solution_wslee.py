class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        res = 0
        dict = {}

        for i in range(len(wall)):
            width_sum = 0
            for j in range(len(wall[i]) - 1):
                # for every row, we consider the sum only
                # up to the second last block, since the
                # last block boundary isn't a valid boundary
                # for the solution
                width_sum += wall[i][j]
                if not width_sum in dict:
                    dict[width_sum] = 1
                else:
                    dict[width_sum] = dict[width_sum] + 1

        res = len(wall)
        for width_sum in dict:
            res = min(res, len(wall) - dict[width_sum])

        return res

#         res = 0
#         dict = {}
#         width_sum = 0
#         for j in range(len(wall[0])):
#             width_sum += wall[0][j]

#         for i in range(len(wall)):
#             for j in range(len(wall[i])):
#                 cumsum = 0
#                 for k in range(0,j+1):
#                     cumsum += wall[i][k]

#                 if not cumsum in dict:
#                     dict[cumsum] = 1
#                 else:
#                     dict[cumsum] =  dict[cumsum] + 1


#         # print(dict)

#         if len(dict) == 1:
#             res = dict[width_sum]
#             return res
#         else:
#             dict.pop(width_sum)
#             res = sorted(dict.items(), key=lambda x: x[1], reverse=True)
#             return len(wall) - res[0][1]

