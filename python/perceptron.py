import numpy as np
import random



w = random.random()
b = random.random()

eta = 0.01
print(w)
print(b)

questions = (
    ([0, 0], -1),
    ([1, 0], 1),
    ([0, 1], 1),
    ([1, 1], 1)
)


def tau(value):
    if value.sum() >= 0:
        return 1
    return -1


notFound = True
while notFound:
    notFound = False
    for q in questions:
        y = tau(np.dot(w, np.array(q[0]).T) + b)
        print(str(q) + " ::: b_" + str(b) + "    w_" + str(w) + " ::: " + str(y))
        if y is not q[1]:
            notFound = True
            w += eta * w
            b += eta * q[1]



print(w)
print(b)