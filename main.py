class Talaba:
    def __init__(self, ball):
        self.__ball = ball

    def get_ball(self):
        return self.__ball

    def set_ball(self, ball):
        self.__ball = ball

t = Talaba(85)
print(t.get_ball())

t.set_ball(95)
print(t.get_ball())
