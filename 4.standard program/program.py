# foo = ['Monty', 'python']
# bar = foo
# foo[1] = 'bodkin'
# print bar
#
# empty = []
# nested = [empty, empty, empty]
# print nested
# nested[1].append('python')
# print nested

# size = 5
# python = ['Python']
# snake_nest = [python] * size
# print snake_nest[0] == snake_nest[1] == snake_nest[2] == snake_nest[3] == snake_nest[4]
# print snake_nest[0] is snake_nest[1] is snake_nest[2] is snake_nest[3] is snake_nest[4]
# import random
# postion = random.choice(range(size))
# snake_nest[postion] = ['python']
# print snake_nest

# mixed = ['cat', '', ['dog'], []]
# for element in mixed:
#     if element:
#         print element
# sent = ['No', 'good', 'fish', 'goes', 'anywhere', 'without', 'a', 'porpoise', '.']
# print all(len(w) > 4 for w in sent)
# print any(len(w) > 4 for w in sent)

# t = 'walk', 'fem', 3
# print t
# print t[0]
# print t[:2]
# print len(t)
#
# raw = 'I turned off the spectroroute'
# text = ['I', 'turned', 'off', 'the', 'spectroroute']
# pair = (6, 'turned')
# print raw[2], text[3], pair[1]
#
# print raw[-3:], text[-3:], pair[-3:]
import nltk
# raw = 'Red lorry, yellow lorry, red lorry, yellow lorry.'
# text = nltk.word_tokenize(raw)
# fdist = nltk.FreqDist(text)
# print list(fdist)
#
# for key in fdist:
#     print fdist[key]
#
# words = ['I', 'turned', 'off', 'the', 'spectroroute']
# words[2], words[3], words[4] = words[3], words[4], words[2]
# print words
# tags = ['noun', 'verb', 'prep', 'det', 'noun']
# print zip(words, tags)

# tokens = nltk.corpus.brown.words(categories='news')
# count = 0
# total = 0
# for token in tokens:
#     count += 1
#     total += len(token)
# print total / count
#
# total = sum(len(t) for t in tokens)
# print total / len(tokens)


# word_list = []
# len_word_list = len(word_list)
# i = 0
# while i < len(tokens):
#     j = 0
#     while j < len_word_list and word_list[j] < tokens[i]:
#         j += 1
#     if j == 0 or tokens[i] != word_list[j]:
#         word_list.insert(j, tokens[i])
#         len_word_list += 1
#     i += 1

# fd = nltk.FreqDist(nltk.corpus.brown.words)
# cumulative = 0.0
# for rank, word in enumerate(fd):
#     cumulative += fd[word] * 100 / fd.N()
#     print '%s %6.2f%% %s' % (rank+1, cumulative, word)
#     if cumulative > 25:
#         break
#
# text = nltk.corpus.gutenberg.words('milton-paradise.txt')
# longest = ''
# for word in text:
#     if len(word) > len(longest):
#         longest = word
# print longest
# maxlen = max(len(word) for word in text)
# print [word for word in text if len(word) == maxlen]
#
# sent = ['the', 'dog', 'gave', 'John', 'the', 'newspaper']
# n = 3
# print [sent[i:i+n] for i in range(len(sent)-n+1)]
# import pprint
# m, n = 3, 7
# array = [[set() for i in range(n)] for j in range(m)]
# array[2][5].add('Alice')
#
# pprint.pprint(array)

# import re
# def get_text(file):
#     """Read text from a file, normalizing whitespace and stripping Html markup"""
#     text = open(file).read()
#     text = re.sub('\s+', ' ', text)
#     text = re.sub(r'<.*?>', ' ', text)
#     return text
# print get_text('./test.html')
#
# print help(get_text)

# def repeat(msg, num):
#     return ' '.join([msg] * num)
# print repeat('Monty Python', 3)
#
# def monty():
#     return "Monty Python"
# print monty()
#
# print repeat(monty(), 3)

# def set_up(word, properties):
#     word = 'lolcat'
#     properties.append('noun')
#     properties = 5

# def tag(word):
#     assert isinstance(word, basestring), "argument to tag() must be a string"
#     if word in ['a', 'the', 'all']:
#         return 'det'
#     else:
#         return 'noun'
# print tag('the')
# print tag('knight')
# print tag(['"Tis"'])

# def freq_words(url, freqdist, n):
#     text = nltk.clean_url(url)
#     for word in nltk.word_tokenize(text):
#         freqdist.inc(word.lower())
#         print freqdist.keys()[n]
constitutution = "http://www.archives.gov/national-archives-experience/charters/constitution_transcript.html"
# fd = nltk.FreqDist()
# freq_words(constitutution, fd, 20)

# def freq_words(url):
#     freqdist = nltk.FreqDist()
#     text = nltk.clean_url(url)
#     for word in nltk.word_tokenize(text):
#         freqdist.inc(word.lower())
#         return freqdist
# fd = freq_words(constitutution)
# print fd.keys()[:20]

# sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the', 'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']
# def extract_property(prop):
#     return [prop(word) for word in sent]
# print extract_property(len)
#
# def last_letter(word):
#     return word[-1]
# print extract_property(last_letter)
#
# print sorted(sent)
# print sorted(sent, cmp)
# print sorted(sent, lambda x, y: cmp(len(y), len(x)))

# def search1(substring, words):
#     result = []
#     for word in words:
#         if substring in word:
#             result.append(word)
#     return result
# def search2(substring, words):
#     for word in words:
#         if substring in word:
#             yield word
# print "search1:"
# for item in search1('zz', nltk.corpus.brown.words()):
#     print item
# print "search2:"
# for item in search2('zz', nltk.corpus.brown.words()):
#     print item

# def permutation(seq):
#     if len(seq) <= 1:
#         yield seq
#     else:
#         for perm in permutation(seq[1:]):
#             for i in range(len(perm)+1):
#                 yield perm[:i] + seq[0:1] + perm[i:]
# print list(permutation(['police', 'fish', 'buffalo']))
#
# def is_content_word(word):
#     return word.lower() not in ['a', 'of', 'the', 'and', 'will', ',', '.']
# sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the', 'sound', 'will', 'take', 'care', 'of', 'themselves', '.']
# print filter(is_content_word, sent)
# print [w for w in sent if is_content_word(w)]
# lengths = map(len, nltk.corpus.brown.sents(categories='news'))
# print sum(lengths) / len(lengths)

# def repeat(msg='<empty>', num=1):
#     return msg * num
# print repeat(num=3)
# print repeat(msg='ALICE')
# print repeat(num=5, msg='alice')
# def generic(*args, **kwargs):
#     print args
#     print kwargs
# print generic(1, "African swallow", monty="python")
#
# song = [['four', 'calling', 'birds'],
#         ['three', 'French', 'hens'],
#         ['two', 'turtle', 'doves']]
# print zip(song[0], song[1], song[2])
# print zip(*song)
#
# def freq_words(file, min=1, num=10):
#     text = open(file).read()
#     tokens = nltk.word_tokenize(text)
#     freqdist = nltk.FreqDist(t for t in token if len(t) >= min)
#     return freqdist.keys()[:num]
# fw = freq_words('ch01.rst', 4, 10)
# fw = freq_words('ch01.rst', min=4, num=10)
# fw = freq_words('ch01.rst', num=10, min=4)

# def find_words(text, wordlength, result=[]):
#     for word in text:
#         if len(word) == wordlength:
#             result.append(word)
#     return result
# print find_words(['omg', 'teh', 'lolcat', 'sitted', 'on', 'teh', 'mat'], 3)
# print find_words(['omg', 'teh', 'lolcat', 'sitted', 'on', 'teh', 'mat'], 2, ['ur'])
#
# import pdb
# pdb.run("find_words(['dog], 3)")
# def factorial(n):
#     result = 1
#     for i in range(n):
#         result *= (i+1)
#     return result
#
# def factorial2(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial2(n-1)

colors = 'rgbmyk' # red, green, blue, cyan, magenta, yellow, black
def bar_chart(categories, words, counts):
    "Plot a bar chart showing counts for each word by category"
    import pylab
    ind = pylab.arange(len(words))
    width = 1 / (len(categories) + 1)
    bar_groups = []
    for c in range(len(categories)):
        bars = pylab.bar(ind+c*width, counts[categories[c]], width, color=colors[c % len(colors)])
        bar_groups.append(bars)
    pylab.xticks(ind + width, words)
    pylab.legend([b[0] for b in bar_groups], categories, loc='upper left')
    pylab.ylabel('Frequency')
    pylab.title('Frequency of Six Modal Verbs by Genre')
    pylab.show()

genres = ['news', 'religion', 'hobbies', 'government', 'adventure']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfdist = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in genres
    for word in nltk.corpus.brown.words(categories=genre)
    if word in modals)
counts = {}
for genre in genres:
    counts[genre] = [cfdist[genre][word] for word in modals]
bar_chart(genres, modals, counts)





















