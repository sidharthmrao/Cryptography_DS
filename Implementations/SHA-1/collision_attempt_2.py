from _sha1 import sha1

from tqdm import tqdm

raw_data = "Hello.".encode("utf-8")
original_data = sha1(raw_data).hexdigest()
data = original_data

i = 1

while True:
    data = sha1(data.encode("utf-8")).hexdigest()
    if data == original_data:
        print("Collision!", f"{i} iterations.")
        break

    if i % 1000000 == 0:
        print(f"On iteration {i}. Current data: {data}")

    i += 1
