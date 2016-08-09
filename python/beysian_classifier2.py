
key_value_list = [
    "comedy", ["fun", "couple", "love", "love"],
    "action", ["fast", "furious", "shoot"],
    "comedy", ["couple", "fly", "fast", "fun", "fun"],
    "action", ["furious", "shoot", "shoot", "fun"],
    "action", ["fly", "fast", "shoot", "love"]
]

word_dict = {}
word_set = set()
total_word_count = 0

for i in range(0, len(key_value_list)):
    if i % 2 == 0:
        if key_value_list[i] not in word_dict:
            word_dict[key_value_list[i]] = []
    if i % 2 == 1:
        key = key_value_list[i - 1]
        values = key_value_list[i]
        for value in values:
            word_dict[key].append(value)
            word_set.add(value)
            total_word_count += 1


classifier = {}

for genre in word_dict.keys():
    if genre not in classifier.keys():
        classifier[genre] = 1

target_words = ["fun", "furious", "fast"]


for genre in classifier.keys():
    for word in target_words:
        print(genre)
        print(((1 + word_dict[genre].count(word)) / (len(word_dict[genre]) + len(word_set))))
        classifier[genre] *= ((1 + word_dict[genre].count(word)) / (len(word_dict[genre]) + len(word_set)))

print(word_dict)
print(classifier)
