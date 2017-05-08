class NGramDist:
    def __init__(self, filename):
        self.gramCount = long(0)
        self.probs = dict()

        for line in open(filename):
            (words, count) = line.split('\t')
            wordlist = words.split(' ')

            self.probs[tuple(wordlist)] = long(count)
            self.gramCount += long(count)

    def get_probability(self, key):
        if key in self.probs:
            return float(self.probs[key]) / self.gramCount
        else:
            return 1.0 / (self.gramCount * 10 ** (len(key[0]) - 2))

#works in python 3
# class NGramDist:
#     def __init__(self, filename):
#         lines = [line.split('\t') for line in open(filename)]
#         self.words = dict(((words.split(" "), int(count)) for (words, count) in lines))
#         self.gramCount = sum(self.words.values())
#
#     def __call__(self, key):
#         if key in self.words:
#             return float(self[key]/self.gramCount)
#         else:
#             return 1.0/self.gramCount * 10 ** (len(key) - 2)
#
#     def __getitem__(self, item):
#         return self.words[item]
#
#     def __iter__(self):
#         return self.words


