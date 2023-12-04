import sys
sys.path.append("C:/Users/admin/Desktop/algo6lab")

def naive_method(haystack, needle):
    comparisons = 0
    haystack_len = len(haystack)
    needle_len = len(needle)
    last_index = -1

    if needle_len == 0:
        return last_index, comparisons

    for i in range(haystack_len - needle_len + 1):
        j = 0

        while j < needle_len:
            comparisons += 1
            if haystack[i + j] != needle[j]:
                break
            j += 1

        if j == needle_len:
            last_index = i

    return last_index, comparisons

haystack = "abcdefgh"
needle = "fgh"
result, comparisons = naive_method(haystack, needle)

if result != -1:
    print(f"Підстрічка: {needle}. Знайдено за позначенням: {result}. Кількість порівнянь: {comparisons}")
else:
    print("Підстрічка не знайдена.")
