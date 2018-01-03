import random

class Character(object):
	def __init__(self, name, movementSpeed, hp, armorclass, strength, dexterity, constitution, intelligence, wisdom,
				 charisma):
		self.name = name
		self.movementSpeed = movementSpeed
		self.MaxHp = hp
		self.CurrentHp = hp
		self.armorclass = armorclass
		self.strength = strength
		self.dexterity = dexterity
		self.constitution = constitution
		self.intelligence = intelligence
		self.wisdom = wisdom
		self.charisma = charisma
		self.strengthModifier = 0
		self.dexterityModifier = 0
		self.constitutionModifier = 0
		self.intelligenceModifier = 0
		self.wisdomModifier = 0
		self.charismaModifier = 0
		self.InitChar()
		self.Weapon = None
		self.WeaponDamage = 1
		self.DamageType = "bludgeoning"

	def InitChar(self):
		self.strengthModifier = self.CalculateModifier(self.strength)
		self.dexterityModifier = self.CalculateModifier(self.dexterity)
		self.constitutionModifier = self.CalculateModifier(self.constitution)
		self.intelligenceModifier = self.CalculateModifier(self.intelligence)
		self.wisdomModifier = self.CalculateModifier(self.wisdom)
		self.charismaModifier = self.CalculateModifier(self.charisma)

	def Attack(self, target):
		D20 = random.randint(1,20)
		Attackroll = D20 + self.strengthModifier
		print ("Attackroll = " + str(Attackroll))
		if Attackroll >= target.armorclass:
			print ('hit')
			TotalDamage = self.Weapon.DamageRoll() + self.strengthModifier
			print (self.name + " Dealt " + str(TotalDamage) + " damage to " + target.name)
			target.SetHealth(target.GetHealth() - TotalDamage)

			print (str(target.CurrentHp) + "/" + str(target.MaxHp))


	def GetHealth(self):
		return self.CurrentHp

	def SetHealth(self, hp):
		self.CurrentHp = hp
		if self.CurrentHp <= 0:
			print (self.name + " has been slain")



	def CalculateModifier(self, Stat):
		Mod = 0;
		while Stat > 1:
			Stat -= 2
			Mod += 1
		Mod -= 5
		return Mod

	def SetWeapon(self, Weapon):
		self.Weapon = Weapon

