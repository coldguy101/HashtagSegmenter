from ngrams.ngram import NGramDist
import math

onegram = NGramDist('one-grams.txt')
bigram = NGramDist('two-grams.txt')


def word_seq_fitness(words):
    prob = sum(math.log10(onegram.get_probability((w,))) for w in words)
    # biProb = sum(math.log10(bigram.get_probability(w)) for w in get_pairs(words))
    # print "Words: " + str(words) + " prob: " + str(10 ** prob)
    # print "biWords: " + str(words) + "prob: " + str(10 ** biProb)
    return prob


def memoize(f):
    cache = {}

    def memoizedFunction(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoizedFunction


@memoize
def segment(word, depth=0):
    if not word:
        return []

    allSegmentations = [[first] + segment(rest, depth + 1) for (first, rest) in split_pairs(word)]

    # allSegmentations = []
    #
    # for (first, rest) in split_pairs(word):
    #     #if word_seq_fitness([first, rest]) != 0:
    #         allSegmentations.append([first] + segment(rest))

    bi_highest_prob = -999999999
    bi_highest_seg = ()

    one_highest_prob = -999999999
    one_highest_seg = ()

    if depth == 0:
        for segmentation in allSegmentations:
            # print "LAST: " + str(segmentation)
            bi_prob_sum = 0
            for w in get_pairs(segmentation):
                # print w,
                p = bigram.get_probability(w)
                # print " prob= " + str(p)
                bi_prob_sum += math.log10(p)
            if bi_prob_sum > bi_highest_prob:
                bi_highest_prob = bi_prob_sum
                bi_highest_seg = segmentation
        print "With BI: " + str(bi_highest_seg)

        # for segmentation in allSegmentations:
        #     probb = word_seq_fitness(segmentation)
        #     if probb > one_highest_prob:
        #         one_highest_prob = probb
        #         one_highest_seg = segmentation
        #
        # if bi_highest_prob < one_highest_prob:
        #     return one_highest_seg
        # else:
        #     return bi_highest_seg

    return max(allSegmentations, key=word_seq_fitness)


def split_pairs(word):
    return [(word[:i + 1], word[i + 1:]) for i in range(len(word))]


def get_pairs(words):
    if type(words) == "string":
        # print "STRING: " + words
        return words
    if len(words) == 1:
        # print "ONE WORD"
        return words
    return [(words[i], words[i + 1]) for i in range(0, len(words) - 1)]


def segment_hash_tag(hashtag):
    if '#' not in hashtag:
        return "not a hashtag"
    hashtag = hashtag.lower()  # change to lower case
    return ("Tag: " + hashtag + " => " + str(segment(hashtag[1:])))


print segment_hash_tag("#iloveyou") + '\n'
print segment_hash_tag("#blessings") + '\n'
print segment_hash_tag("#followme") + '\n'
print segment_hash_tag("#giveaway") + '\n'
print segment_hash_tag("#FreebieFriday") + '\n'
print segment_hash_tag("#instalike") + '\n'
print segment_hash_tag("#hottest") + '\n'
print segment_hash_tag("#touchdownsandmoretouchdowns") + '\n'
print segment_hash_tag("#whatsoeveryoudototheleastofmybrothersthatyoudountome") + '\n'
print segment_hash_tag("#headdressgirl") + '\n'
print segment_hash_tag("#earringsoftheday") + '\n'
print segment_hash_tag("#seguinselfie") + '\n'
print segment_hash_tag("#trendykiddles") + '\n'
print segment_hash_tag("#kindalate") + '\n'
print segment_hash_tag("#bridetobe") + '\n'
print segment_hash_tag("#eventprofs") + '\n'
print segment_hash_tag("#dcevents") + '\n'
print segment_hash_tag("#kindiscool") + '\n'
print segment_hash_tag("#prosocialbehavior") + '\n'
print segment_hash_tag("#bcauseicare") + '\n'
print segment_hash_tag("#memories") + '\n'
print segment_hash_tag("#dancertified") + '\n'
print segment_hash_tag("#ilovesnails") + '\n'

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
