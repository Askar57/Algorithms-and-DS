def two_sum(nums, target):
    num_dict = {}

    for i, num in enumerate(nums):
        # Вычисляем разницу между целевым значением и текущим числом
        difference = target - num

        # Проверяем, если разница уже есть в словаре
        if difference in num_dict:
            # Если есть, возвращаем индексы текущего числа и числа из словаря
            return [num_dict[difference], i]

        # Если разницы нет в словаре, добавляем текущее число и его индекс в словарь
        num_dict[num] = i
        print(num_dict)
    return None


nums1 = [11, 15, 2, 7]
target1 = 9
print()
print(two_sum(nums1, target1))

# nums2 = [3, 2, 4]
# target2 = 6
# print()
# print(two_sum(nums2, target2))

# nums3 = [3, 3]
# target3 = 6
# print()
# print(two_sum(nums3, target3))
