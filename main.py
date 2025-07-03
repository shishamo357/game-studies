import pyxel
from player import Player
from bullet import Bullet

class Game:
    def __init__(self):
        pyxel.init(160, 120, title="My Shooting Game")

        self.player = Player(75, 100)
        self.bullets = []  # 弾追加
        self.enemies = []

        self.score = 0
        self.frame_count = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

        # スペースキーが押したら弾を発射
        if pyxel.btnp(pyxel.KEY_SPACE):
            x, y = self.player.x + 3, self.player.y  # 弾の出現位置を調整
            self.bullets.append(Bullet(x, y))

        # 弾の移動と画面外
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.y < -4:
                self.bullets.remove(bullet)

            # 敵をランダムに出現させる
            # 30フレームごとに敵を出現
        if pyxel.frame_count % 30 == 0:
            x = random.randint(0, pyxel.width - 8)
            self.enemies.append(Enemy(x, -8))

        # 敵の移動
        for enemy in self.enemies[:]:
            enemy.update()
            if enemy.y > pyxel.height:
                self.enemies.remove(enemy)

    def draw(self):
        pyxel.cls(0)
        self.player.draw()

        # 弾の描画
        for bullet in self.bullets:
            bullet.draw()

        for enemy in self.enemies:
            enemy.draw()

if __name__ == "__main__":
    Game()
