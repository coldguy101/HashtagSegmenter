from ngrams.ngram import NGramDist
import math

onegram = NGramDist('one-grams.txt')
bigram = NGramDist('two-grams.txt')


def word_seq_fitness(words):
    prob = sum(math.log10(onegram.get_probability((w,))) for w in words)
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

    bi_highest_prob = -999999999
    bi_highest_seg = ()
    bi_highest_count = 0

    one_highest_prob = -999999999
    one_highest_seg = ()

    if depth == 0:
        for segmentation in allSegmentations:
            # print "LAST: " + str(segmentation)
            bi_prob_sum = 0
            total_count = 0
            for w in get_pairs(segmentation):
                # print w,
                p = bigram.get_probability(w)
                # print " prob= " + str(p)
                bi_prob_sum += math.log10(p)
                total_count += bigram.get_count(w)
            if bi_prob_sum > bi_highest_prob:
                bi_highest_prob = bi_prob_sum
                bi_highest_seg = segmentation
                bi_highest_count = total_count
        print "With BI: " + str(bi_highest_seg)

        maxx = max(allSegmentations, key=word_seq_fitness)

        if bi_highest_count > onegram.get_count(tuple(maxx)):
            print "CORRECT " + str(bi_highest_seg)
        else:
            print "CORRECT " + str(maxx)

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
print segment_hash_tag("#iswamintheafterbirth") + '\n'
print segment_hash_tag("#afterbirth") + '\n'
print segment_hash_tag("#brainstorm") + '\n'
print segment_hash_tag("#lovesnails") + '\n'
print segment_hash_tag("#thx")
