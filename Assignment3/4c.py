import random
from collections import Counter
import matplotlib.pyplot as plt


M = 10000
p = 10007
n = 100

def gen_sk(k: int):
    sk = [i * n for i in range(k)]
    for _ in range(k, n):
        sk.append(random.randint(0, M - 1))
    return sk

def H(Sk: list):
    return [s % n for s in Sk]


def Hr(Sk: list):
    r = random.randint(1, p - 1)
    return [(r * s % p) % n for s in Sk]


def get_max_length(hashes: list):
    counts = Counter(hashes)
    return counts.most_common(1)[0][1]


if __name__ == "__main__":
    H_vals, Hr_vals = [], []
    for k in range(1, n + 1):
        Sk = gen_sk(k)
        H_vals.append(get_max_length(H(Sk)))
        Hr_vals.append(get_max_length(Hr(Sk)))

    ax = plt.axes()
    ax.set_xlabel("k")
    ax.set_ylabel("max chain length")
    ax.set_title("Plot of max chain length versus k")
    ax.plot(H_vals, label="H(.)")
    ax.plot(Hr_vals, label="$H_r(.)$")
    ax.legend()
    plt.savefig("4c.png")
