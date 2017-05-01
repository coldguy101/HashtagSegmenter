import math
from Trie import Trie


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


singleWordProb = OneGramDist('one-grams.txt')


def wordSeqFitness(words):
    prob = sum(math.log10(singleWordProb(w)) for w in words)
    print "Words: " + str(words) + " prob: " + str(prob)
    return prob


def segment(word):
    if not word:
        return []

    allSegmentations = [[first] + segment(rest) for (first, rest) in splitPairs(word)]

    # allSegmentations = []
    # for (first, rest) in splitPairs(word):
    #     ex = [first] + segment(rest)
    #     print ex
    #     allSegmentations.append(ex)

    return max(allSegmentations, key=wordSeqFitness)


def segmentWithProb(word):
    segmented = segment(word)
    return (wordSeqFitness(segmented), segmented)


def splitPairs(word, maxLen=20):
    return [(word[:i + 1], word[i + 1:]) for i in range(max(len(word), maxLen))]


def segmentHashTag(hashtag):
    if '#' not in hashtag:
        return "not a hashtag"
    hashtag = hashtag.lower()  # change to lower case
    return segment(hashtag[1:])

print segmentHashTag("#hellotherebud")

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
