import _sha256

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
