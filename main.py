number = 13

mask = 1 << 3

bit_enabled = (number & mask) != 0

result = number << 3

print(f"3-й біт увімкнений: {bit_enabled}, Число 13 * 8: {result}")