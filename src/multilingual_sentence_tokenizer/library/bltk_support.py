from bltk.langtools import Tokenizer

def sentence_tokenize(text:str):    
    tokenizer = Tokenizer()
    sentences = tokenizer.sentence_tokenizer(text)
    return sentences