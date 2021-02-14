from animal import Animal


class Cat(Animal):
    def __init__(self):
        self.hair = "短发"
        super().__init__()

    def catSkills(self):
        print("捉老鼠")

    def skills(self):
        print("这只动物会喵喵叫")



if __name__ == '__main__':
    cat = Cat()
    cat.catSkills()
    cat.skills()
