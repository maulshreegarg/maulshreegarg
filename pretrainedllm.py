from transformers import pipeline;
ke="sk-proj-IMPBA6aEznIlhj44DVSDT3BlbkFJRX5SlwrecueccmvAS7tU"

#for semantic analysis
classifier=pipeline(task='sentiment-analysis',model='siebert/sentiment-roberta-large-english')
print(classifier("this is bad"))
list=['i love you',' you suck','bad food']
print(classifier(list))

#for summarisation
classifier=pipeline(task='summarization',model='facebook/bart-large-cnn')
print(classifier(" you want to predict sentiment for your own data, we provide an example script via Google Colab. You can load your data to a Google Drive and run the script for free on a Colab GPU. Set-up only takes a few minutes. We suggest that you manually label a subset of your data to evaluate performance for your use case. For performance benchmark values across various sentiment analysis contexts, please refer to our paper "))
