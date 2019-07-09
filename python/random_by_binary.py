from random import randrange


def get_zero_or_one():
    return randrange(2)


def get_random(max_number):
    if max_number <= 1:
        return 0

    random_num = 0
    bit = 1
    while True:
        bit = bit << 1
        random_num = random_num << 1
        random_num += get_zero_or_one()
        if bit >= max_number:
            # 범위 초과시 처음부터 다시 시작
            if random_num >= max_number:
                random_num = 0
                bit = 1
            else:
                break
    return random_num


# Test code
def test_get_random_when(number):
    print("=== number: " + str(number) + " ===")
    tries = 10000
    l = []
    for i in range(tries):
        l.append(get_random(number))
    count_sum = 0
    for i in range(number):
        print(i, ":", l.count(i))
        count_sum += l.count(i)
    for i in l:
        if i >= number:
            print(i)
        if i < 0:
            print(i)
    print(count_sum)
    assert count_sum == tries


test_get_random_when(1)
test_get_random_when(2)
test_get_random_when(3)
test_get_random_when(4)
test_get_random_when(5)
test_get_random_when(10)
test_get_random_when(50)
