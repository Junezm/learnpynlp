import nltk
# text = nltk.word_tokenize("And now for something completely different")
# print nltk.pos_tag(text)
#
# text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
# print nltk.pos_tag(text)
#
# text = nltk.word_tokenize("to ski and to race")
# print nltk.pos_tag(text)
#
# text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
# print text.similar('woman')
# print text.similar('bought')
# print text.similar('over')
# print text.similar('the')

# tagged_token = nltk.tag.str2tuple('fly/NN')
# print tagged_token
# sent = '''
#  The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
#  other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
#  Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PP
#  said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/R
#  accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
#  interest/NN of/IN both/ABX governments/NNS ''/'' ./.
# '''
# print [nltk.tag.str2tuple(t) for t in sent.split()]
#
# print nltk.corpus.brown.tagged_words()
# # print nltk.corpus.brown.tagged_words(simplify_tags=True)
#
# print nltk.corpus.nps_chat.tagged_words()
# print nltk.corpus.conll2000.tagged_words()
# print nltk.corpus.treebank.tagged_words()
# nltk.download('sinica_treebank')
# print nltk.corpus.sinica_treebank.tagged_words()
# nltk.download('mac_morpho')
# print nltk.corpus.mac_morpho.tagged_words()

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
    if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())

tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
for tag in sorted(tagdict):
    print tag, tagdict[tag]

from nltk.corpus import brown
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print w1, w2, w3
for tagged_sent in brown.tagged_sents():
    process(tagged_sent)


















