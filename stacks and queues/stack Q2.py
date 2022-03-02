
from stack import *

"""
Write a function in python that checks if paranthesis 
in the string are balanced or not. 
Possible parantheses are "{}',"()" or "[]". 
Use Stack class from the tutorial.

INPUT OUTPUT
is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
"""


class Solution:
    def match(self, right, left):
        match_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        return match_dict[right] == left

    def answer(self, input) -> bool:
        pstack = stack()
        left_elem = ["(", "[", "{"]
        right_elem = [")", "]", "}"]
        for i in input:
            # load the stack with only left side elem.
            if i in left_elem:
                pstack.push(i)
                # print(pstack)
            # now the right elem and matching them.
            # if the matching fails false cases
            elif i in right_elem:
                if self.match(i, pstack.peek()) == False:
                    return False
                elif pstack.size() == 0:
                    return False
                pstack.pop()

        return pstack.is_empty()


input = ["({a+b})",
         "))((a+b}{",
         "((a+b))",
         "))",
         "[a+b]*(x+2y)*{gg+kk}"]
answer = [True, False, True, False, True]
sol = Solution()
for index, value in enumerate(input):
    if sol.answer(value) == answer[index]:
        print("Passed")
    else:
        print("Failed")
