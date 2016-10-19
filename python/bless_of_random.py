import random
import time
targets = [1,2,3,4,5,6,7,8,9,10,11,12,13]


def pick_me_up(waiting_members, pick_count):
    for i in range(0, pick_count):
        # 긴장감을 위해서 슬립을 건다.
        time.sleep(5)
        if i == pick_count - 1:
            # 마지막 멤버인 만큼 더욱더 긴장감을 주기 위함
            time.sleep(5)
        print(waiting_members.pop(random.randint(0, len(waiting_members) - 1)))


pick_me_up(targets, 10)
