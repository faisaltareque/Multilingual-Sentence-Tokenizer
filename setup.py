from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="multilingual_sentence_tokenizer",
    description="Sentence Tokenizer with Multilingual Support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=[
        "nltk",
        "pysbd",
        "spacy",
        "bltk @ git+https://github.com/faisaltareque/bltk",
        "indic_sentence_tokenizer @ git+https://github.com/faisaltareque/indic_sentence_tokenizer",
        "zh_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/zh_core_web_sm-3.4.0/zh_core_web_sm-3.4.0.tar.gz",
        "xx_ent_wiki_sm @ https://github.com/explosion/spacy-models/releases/download/xx_ent_wiki_sm-3.4.0/xx_ent_wiki_sm-3.4.0.tar.gz",
        "kss",
        "nlpashto"
    ],
    extras_require ={
        "dev":[
            "pytest >=3.7",
        ]
    },
    python_requires='>=3.6',
)
