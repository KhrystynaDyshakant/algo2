from find_k_largest import find_k_largest

nums_1 = [15, 7, 22, 9, 36, 2, 42, 18]
nums_2 = [1, 2, 3, 4, 5]
nums_3 = [1, 1, 1, 1, 1]


result_1 = find_k_largest(nums_1, 2)
result_2 = find_k_largest(nums_2, 2)
result_3 = find_k_largest(nums_3, 1)


print(f"1-й найбільший елемент та його позиція для nums_1: {result_1}")
print(f"2-й найбільший елемент та його позиція для nums_2: {result_2}")
print(f"1-й найбільший елемент та його позиція для nums_3: {result_3}")
