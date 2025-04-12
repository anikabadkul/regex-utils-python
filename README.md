# NLP Project: Text Cleaning and N-Gram Analysis

This project explores foundational Natural Language Processing (NLP) skills through the analysis of a raw text file. The main objectives are:

- Clean and preprocess raw textual data  
- Tokenize the text into words  
- Analyze word and bigram frequencies  
- Visualize word frequency distributions  
- Reflect on linguistic patterns in the selected document

## Text Source

The text analyzed in this project is Chapter 1 from *Pride and Prejudice* by Jane Austen, obtained from Project Gutenberg:

https://www.gutenberg.org/files/1342/1342-0.txt

## Data Loading and Preprocessing

The text was loaded using Python with `ISO-8859-1` encoding to handle character compatibility. Preprocessing involved:

- Lowercasing all text  
- Removing punctuation, numbers, and special characters using regular expressions  
- Normalizing whitespace

## Tokenization

The `nltk` library’s `word_tokenize` function was used to break the cleaned text into word-level tokens.

## Unigram Analysis

Word frequencies were calculated using the `Counter` class. The 10 most frequent unigrams were visualized in a bar chart. Vocabulary statistics computed include:

- Total words  
- Unique words  
- Average word length  
- Vocabulary richness (unique/total)

## Bigram Analysis

Two-word sequences (bigrams) were generated using `nltk.util.ngrams`. Bigrams were filtered to exclude common stopwords for more meaningful results. The top 10 filtered bigrams were printed and interpreted.

## Visualization

- A bar plot showed the top 10 most common unigrams  
- A word cloud (optional) displayed overall word frequency visually

## Reflection

- The most frequent words were common stopwords, though bigram filtering improved interpretability  
- The vocabulary richness score suggested a moderate range of vocabulary  
- Future improvements could include stopword removal during unigram analysis and comparison across multiple chapters

## Tools Used

- Python 3.11  
- `nltk`, `re`, `collections.Counter`, `matplotlib`, `wordcloud`
