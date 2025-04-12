import re 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
nltk.download('punkt')
with open("1342-0.txt", "r", encoding="ISO-8859-1") as file:
    data = file.read()

data = data.lower()
data = re.sub(r'[^a-z\s]', '', data)
data = re.sub(r'\s+', ' ', data).strip()
tokens = word_tokenize(data)
unigrams = list(ngrams(tokens, 1))

#print("Unigrams:", unigrams)
unigram_counts = Counter(unigrams)
print("Top 10 Words:")
for word, count in unigram_counts.most_common(10):
    print(word[0], "→", count)

flat_counts = Counter(tokens)

print(flat_counts.most_common(10))
total_words = len(tokens)
unique_words = len(set(tokens))
avg_word_length = sum(len(word) for word in tokens) / total_words
voab = unique_words/total_words

print("Total words:", total_words)
print("Unique words:", unique_words)
print("Average word length:", round(avg_word_length, 2))
print("Vocabulary richness:", round(voab, 4))


word_freq = Counter(tokens)
common_words = word_freq.most_common(10)

words = [word for word, count in common_words]
counts = [count for word, count in common_words]

plt.figure(figsize=(10, 6))
plt.bar(words, counts)
plt.title("Top 10 Most Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Text")
plt.show()

bigrams = list(ngrams(tokens, 2))
bigram_counts = Counter(bigrams)

print("Top 10 Bigrams:")
for pair, count in bigram_counts.most_common(10):
    print(f"{pair[0]} {pair[1]} → {count}")
          

