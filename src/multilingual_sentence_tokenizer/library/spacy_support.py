import spacy


def sentence_tokenize(text:str, lang:str):
    """
    Chinese
    Nepali
    Indonesian
    Ukrainian
    """
    if lang =='zh':
        nlp = spacy.load('zh_core_web_sm')
        nlp.add_pipe('sentencizer')
        doc = nlp(text)
        return [sent.text for sent in doc.sents]
    else:
        nlp = spacy.load('xx_ent_wiki_sm')
        nlp.add_pipe('sentencizer')
        doc = nlp(text)
        return [sent.text for sent in doc.sents]