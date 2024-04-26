import nltk
from nltk.tokenize import word_tokenize
nltk.download('maxent_ne_chunker')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')
para="Eiffel tower was built from 1220 to 1780 and it was a labour intensive process. I am Tina and i hate life."
words=word_tokenize(para)
tagg=nltk.pos_tag(words)
print(nltk.ne_chunk(tagg).draw())
