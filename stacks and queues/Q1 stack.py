from stack import *
# importing the stack form my implementation.

'''
Question 1: Reverse a string using a stack.
input: Hello World!
output: !dlroW olleH
'''


class Solution:
    def answer(input_str) -> str:
        # Creating the stack form input.
        istack = stack()
        for i in input_str:
            istack.push(i)

        # answer starts here
        ans = ""
        for i in range(0, istack.size()):
            ans += str(istack.pop())

        return ans


input = "Hello World!"
print(input)
print(Solution.answer(input))
