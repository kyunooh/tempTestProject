
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
            word_dict[key_value_list[i]] = {}
    if i % 2 == 1:
        key = key_value_list[i - 1]
        values = key_value_list[i]
        for value in values:
            if value not in key:
                word_dict[key][value] = 1
            else:
                word_dict[key][value] += 1
            word_set.add(value)
            total_word_count += 1


target_words = ["fun", "furious", "fast"]

classifier = {}

for w in word_dict.keys():
    classifier[w] = 1

for t in target_words:
    for key in word_dict.keys():
        for word in word_dict[key]:
            print(word_dict[key])




print(word_dict)
print(word_set)
print(total_word_count)