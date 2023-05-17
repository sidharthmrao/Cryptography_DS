from random import randint


def mtma(p, g, B):
    compute_table = {}
    multiplied_compute_table = {}

    iters = 0

    def gen_num():
        n = randint(0, p)
        if n in compute_table.keys():
            return gen_num()
        return n

    while iters < p:
        iters += 1
        i = gen_num()

        num = (g ** i) % p
        num_multiplied = (num * B) % p

        compute_table[num] = i
        multiplied_compute_table[num_multiplied] = i

        if num in multiplied_compute_table.keys():
            compute_table_val = compute_table[num]
            multiplied_compute_table_val = multiplied_compute_table[num]

            return iters, (compute_table_val - multiplied_compute_table_val) % p

        if num_multiplied in compute_table.keys():
            compute_table_val = compute_table[num_multiplied]
            multiplied_compute_table_val = multiplied_compute_table[num_multiplied]

            return iters, (compute_table_val - multiplied_compute_table_val) % p

    return None
