def levenshtein(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # حذف
                dp[i][j - 1] + 1,  # درج
                dp[i - 1][j - 1] + cost  # جایگزینی
            )
    return dp[m][n]


# خواندن فایل‌ها
with open("Dic.txt", encoding='utf-8') as f:
    dictionary = [line.strip() for line in f.readlines()]

with open("Test.txt", encoding='utf-8') as f:
    test_words = [line.strip() for line in f.readlines()]

# مقایسه و ساخت جدول نتایج
results = []
for test_word in test_words:
    distances = [(word, levenshtein(test_word, word)) for word in dictionary]
    distances.sort(key=lambda x: x[1])  # مرتب‌سازی بر اساس فاصله
    best_match = distances[:3]  # ۳ کاندید نزدیک
    results.append((test_word, best_match))

# نمایش جدول
print("{:<10} {:<15} {:<10}".format("کلمه", "کاندید", "فاصله"))
print("=" * 40)
for test_word, matches in results:
    for word, dist in matches:
        print("{:<10} {:<15} {:<10}".format(test_word, word, dist))
    print("-" * 40)
