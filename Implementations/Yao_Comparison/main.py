import _sha256
import random

bit_length = 100


def get_hash(string):
    return _sha256.sha256(string.encode()).hexdigest()


def alice(num):
    num = bin(num)[2:]
    num = '0' * (bit_length - len(num)) + num

    sub_strings = []

    for i in range(len(num)):
        if num[i] == '1':
            sub_strings.append(get_hash(num[:i + 1]))

    return sub_strings


def bob(num):
    num = bin(num)[2:]
    num = '0' * (bit_length - len(num)) + num

    sub_strings = []

    for i in range(len(num)):
        if num[i] == '0':
            string = num[:i + 1][:-1] + '1'
            sub_strings.append(get_hash(string))

    return sub_strings


a = set(alice(183473))
b = set(bob(183448))

print(a.intersection(b))

valid = 0

for i in range(100):
    num_a = random.randint(0, 999999999)
    num_b = random.randint(0, 999999999)

    real = num_a > num_b
    est = len(set(alice(num_a)).intersection(set(bob(num_b)))) > 0

    if real == est:
        valid += 1

print(valid)


