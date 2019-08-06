class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def erase_braket(string):
            num_start, count, substring_start, substring_end, num_left, num_right = 0, 0, 0, 0, 0, 0
            
            while string[num_start].isalpha():
                num_start += 1
            
            while string[num_start:][count].isdigit():
                count += 1
                
            while string[substring_start] != "[":
                substring_start += 1
            
            while (num_left > num_right) or (num_left == 0):
                if string[substring_end] == "[":
                    num_left += 1
                elif string[substring_end] == "]":
                    num_right += 1
                substring_end += 1
                
            string_left, string_right, leftover = string[:num_start], string[substring_start+1:substring_end-1], string[substring_end:]
            
            num = int(string[num_start:num_start+count])
            return string_left + num*string_right + leftover
            
        while "[" in s:
            s = erase_braket(s)
        return s