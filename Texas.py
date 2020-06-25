class texas_cards:

    def __init__(self, cards: str):

        self.cards_list = []
        self.rank = 0
        self.cards = cards
        self.extract()
        self.showdown()

    def extract(self):
        # 提取五张牌
        i = 1
        while i <= 13:
            str1 = self.cards[i:i + 2]
            self.cards_list.append(str1)
            i += 3

    def showdown(self):
        color = []
        size = []
        size1 = []
        # 提取五张牌的花色
        for k in range(1, 6):
            color.append(str(self.cards_list[k - 1][1]))
        # 提取五张牌的大小
        for h in range(1, 6):
            size4 = size5 = str(self.cards_list[h - 1][0])
            if size5 == "J":
                size4 = size5 = 11
            elif size5 == "T":
                size4 = size5 = 10
            elif size5 == "Q":
                size4 = size5 = 12
            elif size5 == "K":
                size4 = size5 = 13
            elif size5 == "A":
                size5 = 1
                size4 = 14
            size.append(int(size5))
            size1.append(int(size4))

        size_set = list(set(size))
        self.size = size1

        # 判断牌
        while color[0] == color[1] == color[2] == color[3] == color[4]:
            if max(size) - min(size) == 4:
                self.rank = 7
                break

            self.rank = 6
            break
        else:
            if size == list(set(size)) and max(size) - min(size) == 4:

                self.rank = 5
            elif len(size) - 1 == len(size_set):

                self.rank = 2
            elif len(size) - 2 == len(size_set):
                for a in range(0, 5):
                    for b in range(0, 3):
                        if size[a] == size_set[b]:
                            size[a] = 0
                            size_set[b] = 0
                last = [x for x in size if x != 0]
                if last[0] == last[1]:

                    self.rank = 4
                else:

                    self.rank = 3


            else:

                self.rank = 1
