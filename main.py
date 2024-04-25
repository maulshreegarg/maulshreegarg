import nltk
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize,word_tokenize,wordpunct_tokenize,TreebankWordTokenizer
corpus = "hello welcome, to my first nlp program's. Please have patience while i learn."
print(corpus)
documents = sent_tokenize(corpus)
print(documents)
word=word_tokenize(corpus)
print(word)
wordp=wordpunct_tokenize(corpus)
print(wordp)
tokenizer=TreebankWordTokenizer()
print(tokenizer.tokenize(corpus))