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

    def get_count(self, key):
        if key in self.probs:
            return self.probs[key]
        else:
            return 0
