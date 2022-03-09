from itertools import product, permutations
import numpy as np

cc_num = "543210******1234"
def lunn_algorithm(nums):
    nums = np.array([int(v) for v in nums])
    weight = np.array([2 if i % 2 ==0 else 1 for i in range(len(nums))])
    totals = nums * weight
    totals = np.array([sum([int(value) for value in str(total)]) if total > 9 else total for total in totals])

    return sum(totals)

# all possible combination
possible_nums = product( list(range(10)), repeat=6) 

results = {}
for nums in possible_nums:
    nums = [str(n) for n in nums]
    nums = ''.join(nums)
    nums = f"543210{nums}1234"
    
    if int(nums) % 123457 != 0:
        continue

    total = lunn_algorithm(nums)

    if total % 10 == 0:
        if total not in results.keys():
            results[total] = []

        results[total].append(nums)
        # print(curr_totals + res, res)

for k, v in results.items():
    print(k, len(v))
    if len(v) == 1:
        print("CTFlearn{" + str(v[0]) + "}")