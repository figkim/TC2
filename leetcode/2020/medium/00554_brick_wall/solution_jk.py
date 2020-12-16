class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        brick_dict = {}

        for row in wall:
            sum_num = 0
            for num in row[:-1]:
                sum_num += num
                if sum_num in brick_dict:
                    brick_dict[sum_num] += 1
                else:
                    brick_dict[sum_num] = 1

                    
        return len(wall) - max(brick_dict.values()) if brick_dict else len(wall)
