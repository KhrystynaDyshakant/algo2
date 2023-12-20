def min_Num_Of_Bananas_Per_Hour(piles, H):
    left, right = 1, max(piles)

    while left <= right:
        mid = left + (right - left) // 2
        hours_needed = 0

        for pile in piles:
            hours_needed += (pile + mid - 1) // mid

        if hours_needed > H:
            left = mid + 1
        else:
            right = mid - 1
    if not (1 <= len(piles) <= 10**4):
        raise ValueError("Довжина списку piles має бути від 1 до 10^4 елементів.")
    
    if not (len(piles) <= H <= 10**9):
        raise ValueError("Змінна H повинна бути в діапазоні від довжини списку piles до 10^9.")
    
    for pile in piles:
        if not (1 <= pile <= 10**9):
            raise ValueError("Кожен елемент списку piles має бути в діапазоні від 1 до 10^9.")

    return left


