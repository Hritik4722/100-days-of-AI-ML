import numpy as np

outcome_2d = np.random.randint(1,7,size=(10000,2))
# print(outcome_2d)

# temp_sum_rolls = []
# for i in outcome_2d:
#     sum = i.sum()
#     temp_sum_rolls.append(sum)
# sum_rolls = np.array(temp_sum_rolls)

sum_rolls = outcome_2d.sum(axis=1)

# print(sum_rolls)
unique_sum, count_sum =np.unique(sum_rolls,return_counts=True)
# print(unique_sum,count_sum)
for i in range(11):
    print(f"sum of {unique_sum[i]} appeared {count_sum[i]} times")
m_common_sum = unique_sum[count_sum.argmax()]
l_common_sum = unique_sum[count_sum.argmin()]
print(f"Most common sum = {m_common_sum} , least common sum = {l_common_sum}")
