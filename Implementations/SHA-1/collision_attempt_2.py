from _sha1 import sha1

from tqdm import tqdm


def hamming_distance(s1, s2):
    return sum([ch1 != ch2 for ch1, ch2 in zip(s1, s2)])


raw_data = str(10101101100100011001001011000110001001000011100010100010010000011100010010010100110001101000100111100101010001000011011100110010010010001111000101000101100101011)
data = bin(int(raw_data, 2)).encode("utf-8")
data = sha1(data).hexdigest()

min_hamming_distance = len(raw_data)
min_hamming_set = ()

for bit in tqdm(range(len(raw_data))):
    for bit2 in range(bit + 1, len(raw_data)):
        for bit3 in range(bit2 + 1, len(raw_data)):
            for bit4 in range(bit3 + 1, len(raw_data)):
                raw = list(raw_data)
                raw[bit] = str(int(raw[bit]) ^ 1)
                raw[bit2] = str(int(raw[bit2]) ^ 1)
                raw[bit3] = str(int(raw[bit3]) ^ 1)
                raw[bit4] = str(int(raw[bit4]) ^ 1)
                raw = "".join(raw)
                data2 = bin(int(raw, 2)).encode("utf-8")
                data2 = sha1(data2).hexdigest()

                h = hamming_distance(data, data2)
                if h < min_hamming_distance:
                    min_hamming_distance = h
                    min_hamming_set = (data, data2)
                    print(min_hamming_distance)

print(min_hamming_distance)
print(min_hamming_set)
