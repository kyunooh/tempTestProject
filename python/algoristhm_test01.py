import unittest


class BirdTestCase(unittest.TestCase):
    def test_define_array(self):
        test_array = define_array("test_array.txt", 6)
        self.assertIn(['Z', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], test_array)
        self.assertIn(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], test_array)

    def test_define_array_with_user_count(self):
        test_array = define_array("test_array.txt", 3)
        self.assertNotIn(['Z', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], test_array)
        self.assertIn(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], test_array)

    def test_match(self):
        user_count = 12
        test_array = define_array("test_array.txt", user_count)
        result = match(test_array)
        print("result  ::::  " + result)
        self.assertIn('1-3,', result)
        self.assertNotIn('2-3,', result)
        self.assertIn('2-8,', result)
        self.assertIn('6-12,', result)
        self.assertNotIn('11-12', result)
        self.assertNotIn('1-1,', result)
        self.assertNotIn('12-6', result)


def match(user_array):
    match_array = []
    user_idx = 1
    target_array = user_array.copy()

    while len(user_array) > 1:
        user = user_array.pop(0)
        min_difference_len = len(user) * 2
        another_idx = 1
        temp_match_array = []
        for another in target_array:
            if user_idx == another_idx:
                another_idx += 1
                continue
            difference_len = len(set(user).symmetric_difference(set(another)))
            if difference_len < min_difference_len:
                min_difference_len = difference_len
                temp_match_array = []
            if min_difference_len == difference_len:
                if user_idx < another_idx:
                    temp_match_array.append(str(user_idx) + "-" + str(another_idx))
            another_idx += 1
        user_idx += 1
        print(user_idx)
        match_array.extend(temp_match_array)

    return ", ".join(match_array)


def define_array(file_name, user_count):
    f = open(file_name, "r")
    hobby_array = []
    lines = f.readlines()
    count = 0
    for line in lines:
        defined_line = line.replace("\n", "")
        one_line = defined_line.split(" ")
        hobby_array.append(one_line)
        count += 1
        if count == user_count:
            break
    f.close()
    return hobby_array


user_count = input("how many user count? ")
user_array = define_array("array.txt", int(user_count))
print(match(user_array))
