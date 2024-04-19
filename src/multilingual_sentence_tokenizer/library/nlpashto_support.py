from nlpashto import Cleaner
cleaner=Cleaner()

def sentence_tokenize(text:str):        
    return cleaner.clean(text, split_into_sentences=True)