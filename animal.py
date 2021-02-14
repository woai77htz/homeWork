class Animal():

    def __init__(self):
        self.name = "tom"
        self.color = "黑色"
        self.age = 2
        self.sex = "boy"

    def skills(self):
        print("这只动物会叫")
        print("这只动物会跑")


if __name__ == '__main__':
    animal = Animal()
    animal.skills()