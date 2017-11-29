from nltk.corpus import names
import random
import nltk


def gender_features(word):
    return {'last_letter': word[-1]}


names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])
featuresets = [(gender_features(n), g) for (n,g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print classifier.classify(gender_features('Neo'))
print classifier.classify(gender_features('Trinity'))
print nltk.classify.accuracy(classifier, test_set)
print classifier.show_most_informative_features(5)


def gender_feature2(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in "abcdefghijklmnopqrstuvwxyz":
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    return features


print gender_feature2('John')








