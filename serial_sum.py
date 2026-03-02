n = 5
total = 0

print("Serial Computation")
for i in range(1, n + 1):
    total += i
    print(f"step {i}: total = {total} ")

print("Final Serial sum is", total)
