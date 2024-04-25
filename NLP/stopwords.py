import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
nltk.download('stopwords')
para="I am the most important person in her life and yet she ignores my existence and i abhor it. The pain it causes me is unimaginable and i wish the pain would not continue to torment and pain me. I want to move on."
#print(sent_tokenize(para))
s=sent_tokenize(para)
sm=[]
ps=PorterStemmer()
for i in range(len(s)):
    w=word_tokenize(s[i])
    for wo in w:
        if(wo not in set(stopwords.words('english'))):
            sm.append(ps.stem(wo))
            set(sm)
    s[i]=' '.join(sm)
print(s)
