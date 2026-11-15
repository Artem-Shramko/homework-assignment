def digital_root(n):
 if n < 10:
  return n

 digit_sum = sum(int(digit) for digit in str(n))
 return digital_root(digit_sum)


number = 9875

print("Цифровий корінь:", digital_root(number))

assert digital_root(9875) == 2
assert digital_root(123) == 6
assert digital_root(9) == 9
assert digital_root(999) == 9
assert digital_root(10) == 1

print("Автотести пройшли успішно")