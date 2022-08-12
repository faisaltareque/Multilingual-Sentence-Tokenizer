import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
def sentence_tokenize(text:str, lang:str):
    print(sent_tokenize(text))
    return sent_tokenize(text)