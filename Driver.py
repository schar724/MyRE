import myre

instr = "abbb"
reg = "ab*|c"

print(f"Input string: {instr}\nRegular expression: {reg}")

result = myre.match(instr, reg)

print(f"Result: {result}")