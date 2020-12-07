class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command = command.replace("()","o").replace("(al)","al")
        return command
        