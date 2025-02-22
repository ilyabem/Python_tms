"""
Дан список строк. С помощью filter() получить список
тех строк из исходного списка, которые являются
палиндромами (читаются в обе стороны одинаково, например,
’abcсba’)
"""
words = ["level", "world", "radar", "python", "madam", "hello"]

def palindrom_words(n):
    return n == n[::-1]
filter_words = list(filter(palindrom_words,words))

print(filter_words)