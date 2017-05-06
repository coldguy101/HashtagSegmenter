import math


class OneGramDist(dict):
    def __init__(self, filename):
        self.gramCount = 0

        for line in open(filename):
            (word, count) = line[:-1].split('\t')
            self[word] = int(count)
            self.gramCount += self[word]

    def __call__(self, key):
        if key in self:
            return float(self[key]) / self.gramCount
        else:
            return 1.0 / (self.gramCount * 10 ** (len(key) - 2))


class BiGramDist(dict):
    def __init__(self, filename):
        self.gramCount = 0

        for line in open(filename):
            (words, count) = line[:-1].split('\t')
            (word1, word2) = words.split(' ')
            self[(word1, word2)] = int(count)
            self.gramCount += self[(word1, word2)]

    def __call__(self, key):
        if key in self:
            return float(self[key]) / self.gramCount
        else:
            return 1.0 / (self.gramCount * 10 ** (len(key) - 2))

singleWordProb = OneGramDist('one-grams.txt')
biGramProb = BiGramDist('two-grams.txt')


def word_seq_fitness(words):
    prob = sum(math.log10(singleWordProb(w)) for w in words)
    print "Words: " + str(words) + " prob: " + str(10 ** prob)
    return prob


def memoize(f):
    cache = {}

    def memoizedFunction(*args):
        print cache
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    #Dont know what this line is doing, probably nothing, but its not harming anything...
    memoizedFunction.cache = cache
    return memoizedFunction


@memoize
def segment(word):
    if not word:
        return []

    allSegmentations = [[first] + segment(rest) for (first, rest) in split_pairs(word)]

    # allSegmentations = []
    # for (first, rest) in splitPairs(word):
    #     ex = [first] + segment(rest)
    #     print ex
    #     allSegmentations.append(ex)

    return max(allSegmentations, key=word_seq_fitness)


#
# def segment_with_probability(word):
#     segmented = segment(word)
#     return (word_seq_fitness(segmented), segmented)


def split_pairs(word):
    return [(word[:i + 1], word[i + 1:]) for i in range(len(word))]


def segment_hash_tag(hashtag):
    if '#' not in hashtag:
        return "not a hashtag"
    hashtag = hashtag.lower()  # change to lower case
    return segment(hashtag[1:])


#print segment_hash_tag("#hellotheregoodlookin")

print split_pairs("hello world")

# from Trie import Trie
#
# trie = Trie()
#
# with open("words.txt") as f:
#     content = f.readlines()
#
# with open("slang.txt") as s:
#     content2 = s.readlines()
#
# content = [x.strip().lower() for x in content]
# content2 = [x.strip().lower() for x in content2]
#
# content.extend(content2)
#
# trie.make_trie(content)
#
# possibleWords = []
#
# example = "#iloveyou"
#
# # Start at 1 to skip the hashtag
# for i in range(1, len(example) + 1):
#     for j in range(i + 1, len(example) + 1):
#         if trie.in_trie(example[i:j]):
#             possibleWords.append(example[i:j])
#
# print possibleWords
