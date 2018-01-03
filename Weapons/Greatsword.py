import random

class Greatsword(object):
	def __init__(self):
		self.DamageType = "Slashing"

	@staticmethod
	def DamageRoll():
		D6_1 = random.randint(1, 6)
		D6_2 = random.randint(1, 6)
		Damage = D6_1 + D6_2
		return Damage

