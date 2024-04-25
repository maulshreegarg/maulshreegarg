
import nltk

#nltk.download('punkt')
import nltk
nltk.download('punkt')  # If not already downloaded

#TOKENIZATION
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

#STEMMING
#porter
WORDS=['eat','eaten','eating','go','history','gone','story']
from nltk.stem import PorterStemmer,RegexpStemmer,SnowballStemmer
st=PorterStemmer()
for w in WORDS:
    print(w+"-->"+st.stem(w))
#regular expression
res=RegexpStemmer('ing$|s$|ed$|able$',min=4)
print(res.stem('eating'))
#snowball stemma
ss=SnowballStemmer('english')
print(ss.stem('fairly')+" "+st.stem('fairly'))


#lemmatizer
nltk.download('wordnet') 
from nltk.stem import WordNetLemmatizer
l=WordNetLemmatizer()
print(l.lemmatize('going',pos='v'))
WORDS=['eat','eaten','eating','go','history','gone','story']
for w in WORDS:
    print(w+"-->"+l.lemmatize(w,pos='v'))