class Solution:
    def evalRPN(self, tokens):
        operators = ['+', '-', '*', '/']
        operand_stack = []
        operand_stack.append(tokens[0])
        #         print(tokens[0])
        idx = 1
        while True:
            if len(operand_stack) == 0 or idx == len(tokens):
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

        if len(operand_stack) == 1:
            return str(operand_stack.pop())
        else:
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

# more simpler solution... 현타오네
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         res = []
#         ops = ['+','-','*', '/']
#         for token in tokens:
#             if token in ops:
#                 n2 = res.pop() # Pop out in reverse order
#                 n1 = res.pop()
#                 res.append(int(eval(str(n1) + token + str(n2)))) # evaluate statement
#             else:
#                 res.append(token) # keep on appending numbers
#         return res[0]