import time

n = 500_000
target = 499_999

numbers_list = list(range(n))

numbers_set = set(numbers_list)

start = time.perf_counter()
target in numbers_list
list_time = time.perf_counter() - start

start = time.perf_counter()
target in numbers_set
set_time = time.perf_counter() - start

print(f"List search: {list_time:.6f} сек")
print(f"Set search: {set_time:.6f} сек")