import random
from Crypto.Util.number import getPrime


class PseudoRandomNumberGenerator:
	def __init__(self, n=(getPrime(1000) * getPrime(1000)), seed=None):
		self.n = n
		self.seed = seed or random.randint(n // 2, n)

	def get_bit(self, x):
		self.seed = (x ** 2) % self.n
		return self.seed % 2

	def get_bits(self, j):
		total = str([self.get_bit(self.seed) for _ in range(j)])

		total = ''
		for i in range(j):
			total += str(self.get_bit(self.seed))
		return total


num_generator = PseudoRandomNumberGenerator()

z = num_generator.get_bits(1000)

num_zero = z.count('0')
num_one = z.count('1')

print('num_zero =', num_zero)
print('num_one =', num_one)
