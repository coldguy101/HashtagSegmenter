from ngrams.ngram import NGramDist
import math

onegram = NGramDist('one-grams.txt')
bigram = NGramDist('two-grams.txt')


def word_seq_fitness(words):
    prob = sum(math.log10(onegram.get_probability(w)) for w in words)
    biProb = sum(math.log10(bigram.get_probability(w)) for w in get_pairs(words))
    print "Words: " + str(words) + " prob: " + str(10 ** prob)
    print "biWords: " + str(words) + "prob: " + str(10 ** biProb)
    return biProb


def memoize(f):
    cache = {}

    def memoizedFunction(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoizedFunction


@memoize
def segment(word):
    if not word:
        return []

    allSegmentations = [[first] + segment(rest) for (first, rest) in split_pairs(word)]

    # allSegmentations = []
    #
    # for (first, rest) in split_pairs(word):
    #     #if word_seq_fitness([first, rest]) != 0:
    #         allSegmentations.append([first] + segment(rest))

    return max(allSegmentations, key=word_seq_fitness)


def split_pairs(word):
    return [(word[:i + 1], word[i + 1:]) for i in range(len(word))]


def get_pairs(words):
    return [(words[i], words[i + 1]) for i in range(0, len(words) - 1)]


def segment_hash_tag(hashtag):
    if '#' not in hashtag:
        return "not a hashtag"
    hashtag = hashtag.lower()  # change to lower case
    return ("Tag: " + hashtag + " => " + str(segment(hashtag[1:])))


print segment_hash_tag("#iloveyou")
# print segment_hash_tag("#blessings")
# print segment_hash_tag("#followme")
# print segment_hash_tag("#giveaway")
# print segment_hash_tag("#FreebieFriday")
# print segment_hash_tag("#instalike")
# print segment_hash_tag("#hottest")
# print segment_hash_tag("#touchdownsandmoretouchdowns")
# print segment_hash_tag("#whatsoeveryoudototheleastofmybrothersthatyoudountome")
# print segment_hash_tag("#headdressgirl")
# print segment_hash_tag("#earringsoftheday")
# print segment_hash_tag("#seguinselfie")
# print segment_hash_tag("#trendykiddles")
# print segment_hash_tag("#kindalate")
# print segment_hash_tag("#bridetobe")
# print segment_hash_tag("#eventprofs")
# print segment_hash_tag("#dcevents")
# print segment_hash_tag("#kindiscool")
# print segment_hash_tag("#prosocialbehavior")
# print segment_hash_tag("#bcauseicare")
# print segment_hash_tag("#memories")
# print segment_hash_tag("#dancertified")
# print segment_hash_tag("#ilovesnails")

#print get_pairs(["hello", "there", "bud"])

#print split_pairs("helloworld")

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
