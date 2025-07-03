# player.pyのやつ
import pyxel

class Player:
    def __init__(self, x, y):
        self.x = x  # プレイヤーのx座標
        self.y = y  # y座標
        self.speed = 2  # 移動速度

    def update(self):
        # 左右の移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.speed
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.speed

        # 画面端で止
        self.x = max(0, min(self.x, pyxel.width - 8))

    def draw(self):
        # プレイヤーを描画（小さ四）
        pyxel.rect(self.x, self.y, 8, 8, 9)  # 青色
