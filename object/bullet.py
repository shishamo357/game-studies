# bullet.py
import pyxel

class Bullet:
    def __init__(self, x, y):
        self.x = x  # 弾のx座標
        self.y = y  # y座標
        self.speed = 4  # 移動速度

    def update(self):
        # 弾を上方向へ
        self.y -= self.speed

    def draw(self):
        # 弾を描画（小縦長の白線）
        pyxel.rect(self.x + 3, self.y, 2, 4, 7)  # ７白色
