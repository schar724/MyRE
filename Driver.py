#########################################################
#
#   Driver file for Assignment 3
#
#   COMP 2613, Fall 2022
#   Janet Leahy
#
#########################################################

# import your custom module
import myre

instr = "abbb"
reg = "ab*|c"

print(f"Input string: {instr}\nRegular expression: {reg}")

result = myre.match(instr, reg)

print(f"Result: {result}")