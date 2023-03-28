def mtma(p, g, B):
    compute_table = {}
    multiplied_compute_table = {}

    for i in range(1, p):
        num = (g ** i) % p
        num_multiplied = (num * B) % p

        compute_table[num] = i
        multiplied_compute_table[num_multiplied] = i

        if num in multiplied_compute_table.keys():
            compute_table_val = compute_table[num]
            multiplied_compute_table_val = multiplied_compute_table[num]

            return i, (compute_table_val - multiplied_compute_table_val) % p

        if num_multiplied in compute_table.keys():
            compute_table_val = compute_table[num_multiplied]
            multiplied_compute_table_val = multiplied_compute_table[num_multiplied]

            return i, (compute_table_val - multiplied_compute_table_val) % p

    return None
