from indic_sentence_tokenizer import sentence_tokenize as st

def sentence_tokenize(text:str, lang:str, delim_pat='auto'):
    sentences = st.sentence_split(text, lang=lang, delim_pat=delim_pat)
    return sentences