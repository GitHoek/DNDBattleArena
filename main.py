from Characters import Character
from Weapons import Greatsword, Greatclub
from Gameloop import Gameloop
import pygame
pygame.init()

Greatsword = Greatsword.Greatsword()
Greatclub = Greatclub.Greatclub()

Knight = Character.Character(name="Knight", movementSpeed=30, hp=52, armorclass=18, strength=16, dexterity=11, constitution=14, intelligence=11, wisdom=11, charisma=15)
Knight.SetWeapon(Greatsword)
Ogre = Character.Character(name= "Ogre", movementSpeed=40, hp=59, armorclass=11, strength=19, dexterity=8, constitution=16,
						   intelligence=5, wisdom=7, charisma=7)
Ogre.SetWeapon(Greatclub)

#while Knight.CurrentHp > 0 and Ogre.CurrentHp > 0:
#	Knight.Attack(Ogre)
#	Ogre.Attack(Knight)

Gameloop = Gameloop.Gameloop()
Gameloop.run()