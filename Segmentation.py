from Trie import Trie

trie = Trie()

with open("words.txt") as f:
    content = f.readlines()

with open("slang.txt") as s:
    content2 = s.readlines()

content = [x.strip().lower() for x in content]
content2 = [x.strip().lower() for x in content2]

content.extend(content2)

trie.make_trie(content)

print trie.in_trie("race")
print trie.in_trie("racecars")
print trie.in_trie("racecar")
print trie.in_trie("ultra")
print trie.in_trie("fine")
print trie.in_trie("boody")
print trie.in_trie("ass")
print trie.in_trie("love")
print trie.in_trie("life")
print trie.in_trie("lyfe")
print trie.in_trie("lmao")
