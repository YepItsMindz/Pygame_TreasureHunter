from setUp.settings import *


class Node(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, level, data, paths):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(pos[0] + TILE_SIZE / 2, pos[1] + TILE_SIZE / 2))
        self.z = Z_LAYER['path']
        self.level = level
        self.data = data
        self.paths = paths
        self.grid_pos = (int(pos[0] / TILE_SIZE), int(pos[1] / TILE_SIZE))

    def can_move(self, direction):
        if direction in list(self.paths.keys()) and int(self.paths[direction][0][0]) <= self.data.unlocked_level:
            return True
