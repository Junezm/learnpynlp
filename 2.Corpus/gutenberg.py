
# import nltk
# from nltk.corpus import gutenberg
#
# # print(nltk.corpus.gutenberg.fileids())
# #
# # emma = nltk.corpus.gutenberg.words('austen-emma.txt')
# # print(len(emma))
#
#
# # print(gutenberg.fileids())
# # emma = gutenberg.words('austen-emma.txt')
# #
# # for fileid in gutenberg.fileids():
# #     num_chars = len(gutenberg.raw(fileid))
# #     num_words = len(gutenberg.words(fileid))
# #     num_sents = len(gutenberg.sents(fileid))
# #     num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
# #     print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid
#
# macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
# print(macbeth_sentences)
# print(macbeth_sentences[1037])
#
# longest_len = max([len(s) for s in macbeth_sentences])
# print(s for s in macbeth_sentences if len(s) == longest_len)
# from nltk.corpus import webtext
#
# for filied in webtext.fileids():
#     print filied, webtext.raw(filied)[:65], '...'

# from nltk.corpus import nps_chat
#
# chatroom = nps_chat.posts('10-19-20s_706posts.xml')
# print chatroom[126]
import nltk
# from nltk.corpus import brown
# print brown.categories()
# print brown.words(categories='news')
#
#
# news_text = brown.words(categories='news')
# fdist = nltk.FreqDist([w.lower() for w in news_text])
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
#
# for m in modals:
#     print m + ':', fdist[m]
#
# cfd = nltk.ConditionalFreqDist(
#     (genre, word)
#     for genre in brown.categories()
#     for word in brown.words(categories=genre)
# )
# genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# cfd.tabulate(conditions=genres, samples=modals)

# from nltk.corpus import reuters
# # print reuters.fileids()
# # print reuters.categories()
# print reuters.categories('training/9865')
# print reuters.categories(['training/9865', 'training/9880'])

# from nltk.corpus import inaugural
# print inaugural.fileids()
#
# cdf = nltk.ConditionalFreqDist(
#     (target, file[:4])
#     for fileid in inaugural.fileids()
#     for w in inaugural.words(fileid)
#     for target in ['america', 'citizen']
#     if w.lower().startswith(target)
# )
# print cdf
# cdf.plot()
# nltk.download('cess_esp')
# print nltk.corpus.cess_esp.words()
# # nltk.download('floresta')
# print nltk.corpus.floresta.words()
#
# nltk.download('udhr')

# from nltk.corpus import udhr
# languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
# cfd = nltk.ConditionalFreqDist(
#   (lang, len(word))
#   for lang in languages
#   for word in udhr.words(lang + '-Latin1'))
# cfd.plot(cumulative=True)
# from nltk.corpus import gutenberg
# raw = gutenberg.raw('burgess-busterbrown.txt')
#
# print raw[1:20]
#
# words = gutenberg.words('burgess-busterbrown.txt')
# print words[1:20]
#
# sents = gutenberg.sents("burgess-busterbrown.txt")
# print sents[1:20]
# from nltk.corpus import PlaintextCorpusReader
# corpus_root = 'D:\learnpynlp'
# wordlists = PlaintextCorpusReader(corpus_root, '.*')
# print wordlists.fileids()
#
# print wordlists.words('.git/config')
# from nltk.corpus import brown
# genre_word = [(genre, word)
#    for genre in ['news', 'romance']
#    for word in brown.words(categories=genre)]
#
# print len(genre_word)
#
# print genre_word[:4]
# print genre_word[-4:]
#
# cfd = nltk.ConditionalFreqDist(genre_word)
# print cfd
# print cfd.conditions()
#
# print cfd['news']
# print cfd['romance']
# print list(cfd['romance'])
# print cfd['romance']['could']


# from nltk.corpus import inaugural
# cfd = nltk.ConditionalFreqDist(
#     (target, fileid[:4])
#     for fileid in inaugural.fileids()
#     for w in inaugural.words(fileid)
#     for target in ['america', 'citizen']
#     if w.lower().startswith(target)
# )
# cfd.plot()

# sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
# print nltk.bigrams(sent)

# def plural(word):
#     if word.endswith('y'):
#         return word[:-1] + 'ies'
#     elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
#         return word + 'es'
#     elif word.endswith('an'):
#         return word[:-2] + 'en'
#     else:
#         return word + 's'
# print plural('fairy')
# print plural('woman')
#
# from nltk.corpus import stopwords
# print stopwords.words('english')


# names = nltk.corpus.names
# print names.fileids()
#
# male_names = names.words('male.txt')
# female_names = names.words('female.txt')
#
# print [w for w in male_names if w in female_names]
#
# cfd = nltk.ConditionalFreqDist(
#     (fileid, name[-1])
#     for fileid in names.fileids()
#     for name in names.words(fileid)
# )
# cfd.plot()

# entries = nltk.corpus.cmudict.entries()
# print len(entries)
#
# for entry in entries[39943:39951]:
#     print entry

# from nltk.corpus import toolbox
# print toolbox.entries('rotokas.dic')
# from nltk.corpus import wordnet as wn
# print wn.synsets('motorcar')
# # print wn.synsets('car.n.01').lemma_names
#
# print wn.lemma('car.n.01.automobile')








