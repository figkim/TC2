class Solution:
    def evalRPN(self, tokens):
        operators = ['+', '-', '*', '/']
        operand_stack = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token in operators:
                # operator
                result = self.compute(operand_stack, token)
                operand_stack.append(result)
            else:
                # operand
                operand_stack.append(token)

            # print(token, operand_stack)

        return int(operand_stack[-1])

    def compute(self, operand_stack, operator):
        second_operand = int(operand_stack.pop())
        first_operand = int(operand_stack.pop())

        #         result = int(eval(first_operand + operator + second_operand))

        if operator == '+':
            result = first_operand + second_operand
        elif operator == '-':
            result = first_operand - second_operand
        elif operator == '*':
            result = int(first_operand * second_operand)
        elif operator == '/':
            result = int(first_operand / second_operand)

        return str(result)