from diaries.AbstractDiary import AbstractDiary

class SakakibaraDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"
    def get_summary(self):
        return "今日は疲れた。明日も頑張ろう。"
    def get_author(self):
        return "Sakakibara"