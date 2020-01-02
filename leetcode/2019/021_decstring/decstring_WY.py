class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def erase_braket(string):
            num_start, count, substring_start, substring_end, num_braket = 0, 0, 0, 1, 1
            
            while string[num_start].isalpha():
                num_start += 1
            
            while string[num_start+count].isdigit():
                count += 1
                
            while string[num_start+count+substring_start] != "[":
                substring_start += 1
            
            while (num_braket > 0):
                if string[num_start+count+substring_end] == "[":
                    num_braket += 1
                elif string[num_start+count+substring_end] == "]":
                    num_braket -= 1
                substring_end += 1
                
            string_left, string_duplicate, string_right = string[:num_start], string[num_start+count+substring_start+1:num_start+count+substring_end-1], string[num_start+count+substring_end:]
            num = int(string[num_start:num_start+count])
            return string_left + num*string_duplicate + string_right
            #return string[:num_start] + int(string[num_start:num_start+count]) * string[num_start+count+substring_start+1:num_start+count+substring_end-1] + string[num_start+count+substring_end:]
        
        while "[" in s:
            s = erase_braket(s)
        return s
    