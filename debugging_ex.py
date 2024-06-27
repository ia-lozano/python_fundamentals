# Debugging with the pdb;pdb.set_trace() module
# Commands:
# * breakpoint: stops the execution
# * continue: continues the execution
# * list: shows the next 11 lines around the current line
# * next: step by step execution
# * p: shows the value of the variable in that line
# * clear: clears the breakpoints if called without parameters, or deletes the break point given as a parameter

import pdb;pdb.set_trace()

total = 0
number = int(input("Enter an integer number: "))
for i in range(number):
    total += i
print(total)

