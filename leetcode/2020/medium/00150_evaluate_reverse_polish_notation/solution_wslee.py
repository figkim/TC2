class Solution:
    def evalRPN(self, tokens):
        operators = ['+', '-', '*', '/']
        operand_stack = []
        operand_stack.append(tokens[0])
        #         print(tokens[0])
        idx = 1
        while True:
            if idx == len(tokens):
                break
            token = tokens[idx]
            if token in operators:
                # operator
                result = self.compute(operand_stack, token)
                operand_stack.append(result)
            else:
                # operand
                operand_stack.append(token)

            idx += 1
        #             print(token, operand_stack)

        return operand_stack[0]

    def compute(self, operand_stack, operator):
        second_operand = int(operand_stack.pop())
        first_operand = int(operand_stack.pop())

        if operator == '+':
            result = first_operand + second_operand
        elif operator == '-':
            result = first_operand - second_operand
        elif operator == '*':
            result = int(first_operand * second_operand)
        elif operator == '/':
            result = int(first_operand / second_operand)

        return result
