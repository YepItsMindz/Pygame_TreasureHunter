from Sprite.animatedSprite import AnimatedSprite
from setUp.settings import *


class Item(AnimatedSprite):
	def __init__(self, item_type, pos, frames, groups, data):
		super().__init__(pos, frames, groups)
		self.rect.center = pos
		self.item_type = item_type
		self.data = data

	def activate(self):
		if self.item_type == 'gold':
			self.data.coins += 5
		if self.item_type == 'silver':
			self.data.coins += 1
		if self.item_type == 'diamond':
			self.data.coins += 20
		if self.item_type == 'skull':
			self.data.coins += 50
		if self.item_type == 'potion':
			self.data.health += 1
