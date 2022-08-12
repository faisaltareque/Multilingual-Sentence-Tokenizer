# Multilingual Sentence Tokenizer

Multilingual Sentence Tokenizer
Supported Languages are:
```bash
'am': Amharic,
'ar': Arabic,
'bg': Bulgarian,
'bn': Bengali,
'zh': Chinese,
'da': Danish,
'de': German,
'el': Greek, 
'en': English,
'es': Spanish,
'fa': Persian,
'fr': French,
'gu': Gujarati,
'hi': Hindi,
'hy': Armenian,
'id': Indonesian,
'it': Italian,
'ja': Japanese,
'kk': Kazakh,
'kn': kannada,
'ml': Malayalam ,
'mr': Marathi,
'my': Burmese,
'ne': Nepali,
'nl': Dutch,
'or': Oriya,
'pa': Punjabi,
'pl': Polish,
'pt': Portuguese,
'ru': Russian,
'si': Sinhala,
'sk': Slovak,
'sl': Slovenian,
'ta': Tamil,
'te': Telugu,
'th': Thai,
'tr': Turkish,
'uk': Ukrainian,
'ur': Urdu,
'vi': Vietnamese,
'yo': Yoruba
```
  

## Setup from Clone
```bash
python setup.py bdist_wheel
pip install -e .
```

## Setup from Git
```bash
pip install git+https://github.com/faisaltareque/multilingual_sentence_tokenizer
```


* **Default usage**


```python
from multilingual_sentence_tokenizer import sentence_tokenizer
#text (str): text to split into sentence
#lang (str): ISO 639-2 language code
sentence_tokenizer.tokenize(text='''Newton took space to be more than relations between material objects and based his position on observation and experimentation. For a relationist there can be no real difference between inertial motion, in which the object travels with constant velocity, and non-inertial motion, in which the velocity changes with time, since all spatial measurements are relative to other objects and their motions.''', language='en')
```


## Library Used
1. [Spacy](https://spacy.io/)  
2. [NLTK](https://www.nltk.org/)  
3. [BLTK](https://pypi.org/project/bltk/)  
4. [Indic NLP Library](https://github.com/anoopkunchukuttan/indic_nlp_library)  
5. [PYSBD](https://github.com/nipunsadvilkar/pySBD)  