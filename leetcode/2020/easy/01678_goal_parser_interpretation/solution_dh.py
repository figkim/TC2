class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        rStr = ''
        while len(command) != 0:
            if command[0] == 'G':
                rStr += 'G'
                command = command[1:]
            elif command[0] == '(':
                if command[1] == ')':
                    rStr += 'o'
                    command = command[2:]
                else:
                    rStr += 'al'
                    command = command[4:]
        return rStr
