from __future__ import division
import nltk, re, pprint

from urllib import urlopen
# url = "http://www.gutenberg.org/files/2554/2554-0.txt"
# raw = urlopen(url).read()
# print type(raw)
# print len(raw)
# print raw[:75]
#
# print raw.find("PART I")
# print raw.rfind('End of Project')
# raw = raw[5303:1157681]
# print raw.find("PART I")

# url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
# html = urlopen(url).read()
# print html[:60]
# raw = nltk.get_text(html)
# print(raw)

# import feedparser
# llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
# print llog['feed']['title']
# print len(llog.entries)
# post = llog.entries[2]
# print post.title
# content = post.content[0].value
# print content[:70]
import os
# f = open('../README.md')
# raw = f.read()
# print raw
# print os.listdir('../')
# f = open('../README.md', 'rU')
# for line in f:
#     print line.strip()
# couple = """hello,how are you?
# I'm fain thank you"""
# print couple
# a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
# b = [' ' * 2 * (7 - i) + 'very' *i for i in a]
# for line in b:
#     print line
# from nltk.corpus import gutenberg
# raw = gutenberg.raw('melville-moby_dick.txt')
# fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
# print fdist.keys()
# fdist.plot()
import codecs
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
# f = codecs.open(path, encoding='latin2')
# for line in f:
#     line = line.strip()
#     print line.encode('unicode_escape')
#
# print ord('a')
# a = u'\u0061'
# print a
#
# nacute = u'\u0144'
# print nacute
# nacute_utf = nacute.encode('utf8')
# print repr(nacute)
# import unicodedata
# lines = codecs.open(path, encoding='latin2').readlines()
# line = lines[2]
# print line.encode('unicode_escape')
# for c in line:
#     if ord(c) > 127:
#         print '%s U+%04x %s' % (c.encode('utf8'), ord(c), unicodedata.name(c))

# -*- coding: utf-8 -*-
import re
# wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
# print wordlist
# print [w for w in wordlist if re.search('ed$', w)]
# print [w for w in wordlist if re.search('^..j..t..$', w)]
# print [w for w in wordlist if re.search('..j..t..', w)]
# print [w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]
# print [w for w in wordlist if re.search('^[g-o]+$', w)]
#
# chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
# print [w for w in chat_words if re.search('^m+i+n+e+$', w)]
#
wsj = sorted(set(nltk.corpus.treebank.words()))
# print [w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)]
# print [w for w in wsj if re.search('^[A-Z]+\$$', w)]
# print [w for w in wsj if re.search('^[0-9]{4}$', w)]
# print [w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)]
# print [w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)]
# print [w for w in wsj if re.search('(ed|ing)$', w)]

# word = 'supercalifragilisticexpialidocious'
# print re.findall(r'[aeiou]', word)
# print len(re.findall(r'[aeiou]', word))
# fd = nltk.FreqDist(vs for word in wsj
#                             for vs in re.findall(r'[aeiou]{2,}', word))
# print fd.items()
#
# print [int(n) for n in re.findall(r'[0-9]+', '2009-12-31')]
# regexp = r'[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
# def compress(word):
#     pieces = re.findall(regexp, word)
#     return ''.join(pieces)
#
# english_udhr = nltk.corpus.udhr.words('English-Latin1')
# print nltk.tokenwrap(compress(w) for w in english_udhr[:75])
#
# rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
# cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
# cfd = nltk.ConditionalFreqDist(cvs)
# # cfd.tabulate()
# # cfd.plot()
# cv_word_pairs = [(cv, w) for w in rotokas_words
#                             for cv in re.findall(r'[ptksvr][aeiou]', w)]
# cv_index = nltk.Index(cv_word_pairs)
# print cv_index['su']
# print cv_index['po']

# def stem(word):
#     for suffix in ['img', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
#         if word.endswith(suffix):
#             return word[:-len(suffix)]
#     return word
#
# print re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
# print re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
# print re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
# print re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')

# from nltk.corpus import gutenberg, nps_chat
# moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
# print moby.findall(r'<a>(<.*>)<man>')
#
# chat = nltk.Text(nps_chat.words())
# print chat.findall(r'<.*><.*><bro>')
# print chat.findall(r'<l.*>{3,}')
# print nltk.re_show(r'shit', 'hello, shit')

# from nltk.corpus import brown
# hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
# print hobbies_learned.findall(r"<as> <\w*> <as> <\w*s>")

# raw = """DENNIS: Listen, strange women lying in ponds distributing swords
# ... is no basis for a system of government. Supreme executive power derives from
# ... a mandate from the masses, not from some farcical aquatic ceremony."""
# tokens = nltk.word_tokenize(raw)
# porter = nltk.PorterStemmer()
# lancaster = nltk.LancasterStemmer()
# print [porter.stem(t) for t in tokens]
# print [lancaster.stem(t) for t in tokens]

# class IndexedText(object):
#     def __init__(self, stemmer, text):
#         self._text = text
#         self._stemmer = stemmer
#         self._index = nltk.Index((self._stem(word), i)
#                                     for (i, word) in enumerate(text))
#     def concordance(self, word, width=40):
#         key = self._stem(word)
#         wc = width/4
#         print self._index
#         for i in self._index[key]:
#             lcontext = ''.join(self._text[i-wc:i])
#             rcontext = ''.join(self._text[i:i+wc])
#             ldisplay = '%*s' % (width, lcontext[-width:])
#             rdisplay = '%-*s' % (width, rcontext[:width])
#             print ldisplay, rdisplay
#     def _stem(self, word):
#         return self._stemmer.stem(word).lower()
#
# porter = nltk.PorterStemmer()
# grail = nltk.corpus.webtext.words('grail.txt')
# text = IndexedText(porter, grail)
# print text.concordance('lie')

# wnl = nltk.WordNetLemmatizer()
# print [wnl.lemmatize(t) for t in tokens]
#
# raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
# ... though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
# ... well without--Maybe it's always pepper that makes people hot-tempered,'..."""
# print re.split(r' ', raw)
# print re.split(r'[ \t\n]+', raw)
# print re.split(r'\W+', raw)
# text = 'That U.S.A. poster-print costs $12.40...'
# pattern = r'(?x)([A-Z]\.)+|\w+(-\w+)*|\$\d+(\.\d+)?%?|\.\.\.|[][.,;\'"?():-_`]'
# nltk.regexp_tokenize(text, pattern)
# print len(nltk.corpus.brown.words()) / len(nltk.corpus.brown.sents())
#
# sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
# sents = sent_tokenizer.tokenize(text)
# pprint.pprint(sents[171:181])

# print "%s wants a %s %s" % ("Lee", "sandwich", "for lunch")

