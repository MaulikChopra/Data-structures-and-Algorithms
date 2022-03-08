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
from stack import *


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
            if i in left_elem:
                pstack.push(i)
                # print(pstack)
            elif i in right_elem:
                if self.match(i, pstack.peek()) == False:  # cornercase 3
                    return False
                elif pstack.size() == 0:  # cornercase 1
                    return False
                pstack.pop()

        if pstack.size() == 0:  # cornercase 2
            return True
        return False
# Or we could have used one liner here as:
#     return pstack.is_empty()


input = ["({a+b})",
         "))((a+b}{",
         "({[(((a+b)))]})",
         "[a+b]*(x+2y)*{gg+kk}",
         "(){}[])",
         "{[[a+b]*}(x+2y)]}"]

# automatic checking code, don't modify.
# returns passed/failed by running our algo.
answer = [True, False, True, True, False, False]
sol = Solution()
for index, value in enumerate(input):
    tempbool = sol.answer(value)
    if tempbool == answer[index]:
        print("Passed,", tempbool)
    else:
        print("Failed,", tempbool)

"""
Pseudo code:
accounting the corner cases for this puzzle.
Corner cases when the test should Fail ie: no balance
1. there are extra right brackets 
2. there are extra left bracket 
3. there is single bracket pair unbalanced 

NOW WRITING THE SUDO CODE:
def match_helper_function(self, rightbracket, leftbracket):
    create a dict with all the matches
    check if the rightbracket matches with the leftbracket using the dict
    return bool

def answer(self, input):
    initialize the stack
    loop traversing the length of string:
        check for the left brackets first:
            add the left bracket to the stack
        check for the right brackets now: 
            check if the rightbracket does not match leftbracket: #corner case 3
                return False
            check if the stack is empty: #corner case 1
                return False
            stack.pop() #to continue traversing
        
    at the end if still there are leftbrackets remaining in the stack then return False
    otherwise True #corner case 2

REMEMBER: there can be multiple correct solutions ans approaches so there is no correct way to implement the solution. 
the only correct way is: To understand the concept of the algorithm, and To get the correct output with best time and space complexity.


TIME COMPLEXITY: O(n) ie: linear time

SPACE COMPLEXITY: O(n) ie: linear space

fact: we are dealing with stack and mostly it takes linear space when dealing with stack/array modification.
"""
