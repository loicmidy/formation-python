# -*- coding: utf-8 -*-
import nltk.tokenize as tk
from nltk.text import Text 
import nltk

raw="""
bonjour
demain
certain
demain
"""
tokens = tk.word_tokenize(raw)

text=nltk.Text(tokens)

text.concordance("demain")