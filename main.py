from Characters import Character
from Weapons import Greatsword, Greatclub
from Gameloop import Gameloop
import pygame
pygame.init()

Greatsword = Greatsword.Greatsword()
Greatclub = Greatclub.Greatclub()

Knight = Character.Character("Knight", 30, 52, 18, 16, 11, 14, 11, 11, 15)
Knight.SetWeapon(Greatsword)
Ogre = Character.Character(name= "Ogre", movementSpeed=40, hp=59, armorclass=11, strength=19, dexterity=8, constitution=16,
						   intelligence=5, wisdom=7, charisma=7)
Ogre.SetWeapon(Greatclub)

while Knight.CurrentHp > 0 and Ogre.CurrentHp > 0:
	Knight.Attack(Ogre)
	Ogre.Attack(Knight)

Gameloop = Gameloop.Gameloop()
Gameloop.run()