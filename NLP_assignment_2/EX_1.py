import re
from collections import Counter

with open('Corpus.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# A
words = re.findall(r'\b\w+\b', text)
total_words = len(words)
print("Total words length: " , total_words)

# B
unique_words = set(words)
unique_word_count = len(unique_words)
print("unique words count: ", unique_word_count)

# C
word_counts = Counter(words)
print("word frequency count: ", word_counts)

# D
question_sentences = re.split(r'[^؟\n]*؟', text)
num_questions = len(question_sentences)
print("the count of sentences with question mark: ", num_questions)