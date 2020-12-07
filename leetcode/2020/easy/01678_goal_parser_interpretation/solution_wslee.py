class Solution:
    def interpret(self, command: str) -> str:
        """
        :type command: str
        :rtype: str
        """
        command = command.replace('(al)', 'al').replace('()', 'o')
        return command