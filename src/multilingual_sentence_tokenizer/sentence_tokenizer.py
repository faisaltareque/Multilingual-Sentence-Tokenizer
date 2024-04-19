from multilingual_sentence_tokenizer.library import spacy_support
from multilingual_sentence_tokenizer.library import bltk_support
from multilingual_sentence_tokenizer.library import indic_support
from multilingual_sentence_tokenizer.library import pysbd_support
from multilingual_sentence_tokenizer.library import nltk_support
from multilingual_sentence_tokenizer.library import kss_support
from multilingual_sentence_tokenizer.library import nlpashto_support
from multilingual_sentence_tokenizer import languages_support

def tokenize(text:str,language:str):
    """
    Tokenize sentences in text
    Arguments:
        text: Document string 
        language: Language ID i.e. ISO:639-2 code. 
    Returns:
        List of strings
    """
    support_library = languages_support.get_support_library(language=language)

    if support_library == 'spacy':
        return spacy_support.sentence_tokenize(text=text, lang=language)
    elif support_library == 'bltk':
        return bltk_support.sentence_tokenize(text=text)
    elif support_library == 'nltk':
        return nltk_support.sentence_tokenize(text=text, lang=language)
    elif support_library == 'indic':
        return indic_support.sentence_tokenize(text=text, lang=language)
    elif support_library == 'pysbd':
        return pysbd_support.sentence_tokenize(text=text, lang=language)
    elif support_library == 'kss':
        return kss_support.sentence_tokenize(text=text)
    elif support_library == 'nlpashto':
        return nlpashto_support.sentence_tokenize(text=text)

    

