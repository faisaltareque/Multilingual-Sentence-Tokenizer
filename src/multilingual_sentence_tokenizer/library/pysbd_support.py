import pysbd
def sentence_tokenize(text:str, lang:str, clean=True):        
    seg = pysbd.Segmenter(language=lang, clean=clean)
    return seg.segment(text)