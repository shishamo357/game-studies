class Enemy:
    def __init__(self, x, y, speed=1):
        self.x = x
        self.y = y
        self.speed = speed  # 敵の落下スピード

    def update(self):
        self.y += self.speed  # 下に移動

    def draw(self):
        pyxel.rect(self.x, self.y, 8, 8, 8)  # 敵
