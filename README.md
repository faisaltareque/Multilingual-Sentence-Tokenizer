# Multilingual Sentence Tokenizer

Multilingual Sentence Tokenizer  
Supported Languages are:
| Language | ISO 639-2 Code |
|----------|----------------|
| Amharic  | am             |
| Arabic   | ar             |
| Bulgarian| bg             |
| Bengali  | bn             |
| Chinese  | zh             |
| Danish   | da             |
| German   | de             |
| Greek    | el             |
| English  | en             |
| Spanish  | es             |
| Persian  | fa             |
| French   | fr             |
| Gujarati | gu             |
| Hindi    | hi             |
| Armenian | hy             |
| Indonesian | id           |
| Italian  | it             |
| Japanese | ja             |
| Kazakh   | kk             |
| Kannada  | kn             |
| Malayalam| ml             |
| Marathi  | mr             |
| Burmese  | my             |
| Nepali   | ne             |
| Dutch    | nl             |
| Oriya    | or             |
| Punjabi  | pa             |
| Polish   | pl             |
| Portuguese | pt           |
| Russian  | ru             |
| Sinhala  | si             |
| Slovak   | sk             |
| Slovenian| sl             |
| Tamil    | ta             |
| Telugu   | te             |
| Thai     | th             |
| Turkish  | tr             |
| Ukrainian| uk             |
| Urdu     | ur             |
| Vietnamese | vi           |
| Yoruba   | yo             |
| Korean   | ko             |
| Pashto   | ps             |
  

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
sentence_tokenizer.tokenize(text='''Newton took space to be more than relations between 
                                    material objects and based his position on observation and experimentation. 
                                    For a relationist there can be no real difference between inertial motion, 
                                    in which the object travels with constant velocity, and non-inertial motion, 
                                    in which the velocity changes with time, since all spatial measurements are 
                                    relative to other objects and their motions.''', language='en')
```


## Library Used
1. [Spacy](https://spacy.io/)  
2. [NLTK](https://www.nltk.org/)  
3. [BLTK](https://pypi.org/project/bltk/)  
4. [Indic NLP Library](https://github.com/anoopkunchukuttan/indic_nlp_library)  
5. [PYSBD](https://github.com/nipunsadvilkar/pySBD)
6. [KSS](https://github.com/likejazz/korean-sentence-splitter)  
7. [NLPashto](https://pypi.org/project/nlpashto/)
