import pykakasi
import csv

# Based on this unicode guide http://www.rikai.com/library/kanjitables/kanji_codes.unicode.shtml
def contains_kanji(word):
    for char in word:
        if char >= "\u4e00" and char <= "\u9faf":
            return True
    return False

file = input('Name of your raw text file: ')
kanji_vocabulary = []
word_list = open(file).readlines()
for line in word_list:
    if contains_kanji(line):
        kanji_vocabulary.append(line.strip())

potential_homophones = {}
kks = pykakasi.kakasi()
kks.setMode("J","H") # Convert Japanese text into hiragana only
converter = kks.getConverter()

'''
create new dict of kanji based words
format
{"あめ": ["雨","飴"]}
'''
for word in kanji_vocabulary:
    kana = converter.do(word)
    if kana in potential_homophones:
        potential_homophones[kana].append(word)
    else:
        potential_homophones[kana] = [word]

# copy dict -- cannot del while iterating. Lists < 2 items are lonely words, not homophones.
homophones = potential_homophones.copy()
for key, value in potential_homophones.items():
    if len(value) < 2:
        del homophones[key]

# write to csv for later use
with open('homophones.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    # each vocab word is a column - no quotes or brackets
    for key in sorted(homophones.keys()):
        writer.writerow([key] + homophones[key])