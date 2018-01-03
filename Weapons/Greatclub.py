import random

class Greatclub(object):
	def __init__(self):
		self.DamageType = "bludgeoning"

	@staticmethod
	def DamageRoll():
		D8_1 = random.randint(1, 8)
		D8_2 = random.randint(1, 8)
		Damage = D8_1 + D8_2
		return Damage

