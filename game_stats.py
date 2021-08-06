class Gamestats:
    """跟踪记录游戏信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 是游戏已开始处于非活动状态
        self.game_active = False

        # 读取文件high_score.txt
        with open('high_score.txt') as high_score_file:
            self.high_score = int(high_score_file.read())

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
