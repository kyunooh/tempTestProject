from random import randrange
get_zero_or_one = lambda: randrange(2)


def get_random(max_number):
    temp = 0
    i = 1
    while True:
        i = i << 1
        temp = temp << 1
        temp += get_zero_or_one()
        if i >= max_number:
            # 범위 초과시 처음부터 다시 시작
            if temp >= max_number:
                temp = 0
                i = 1
            else:
                break
    return temp


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
