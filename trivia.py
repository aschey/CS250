import csv


class TriviaCard:

    def __init__(self, question, answer):
        self._question = question
        self._answer = answer

    def get_question(self):
        return self._question

    def is_answer(self, answer):
        return self._answer == answer


class TriviaGame:

    def __init__(self, filename):
        self._filename = filename
        self._cards = []

    def _make_card(self, data):
        return TriviaCard(data[0], data[1])

    def _read_cards(self):
        with open(self._filename, 'rt') as f:
            for row in csv.reader(f):
                card = self._make_card(row)
                self._cards.append(card)

    def _draw_card(self):
        card = self._cards[0]
        self._cards.pop(0)
        self._cards.append(card)
        return card

    def _play_round(self):
        card = self._draw_card()
        question = card.get_question()
        response = input(question + ' ')
        while not card.is_answer(response):
            print(response, 'is not the correct answer!\n')
            response = input(question + ' ')
        print(response, 'is the correct answer!\n')

    def play(self, num_rounds):
        self._read_cards()
        for i in range(num_rounds):
            print('--- Round', str(i + 1), 'of', num_rounds,'---\n')
            self._play_round()

class ThemedTriviaCard(TriviaCard):
    def __init__(self, question, answer, theme):
        super().__init__(question, answer)
        self._theme = theme

    def has_theme(self, theme):
        return self._theme == theme

class ThemedTriviaGame(TriviaGame):
    def _make_card(self, data):
        return ThemedTriviaCard(data[0], data[1], data[2])

class SingleThemedTriviaGame(ThemedTriviaGame):
    def __init__(self, filename, theme):
        super().__init__(filename)
        self._theme = theme
    
    def _read_cards(self):
        with open(self._filename, "rt") as f:
            for row in csv.reader(f):
                card = self._make_card(row)
                if card.has_theme(self._theme):
                    self._cards.append(card)


def main(args):
    if len(args) < 2:
        return 'Usage: {0} number-of-rounds'.format(args[0])
    game = SingleThemedTriviaGame('cards.txt', 'Entertainment')
    print('--- Play game ---\n')
    game.play(int(args[1]))
    print('--- Game over ---')

dct = {'jedoe':['John','E.','Doe'], 'prince':['Prince'],'jdoe':['Jane','Doe'],
        'defresh':['Doug','E.','Fresh']}
def unique_value_strings(dct):
    uniques = []
    for valList in dct.values():
        for val in valList:
            if val not in uniques:
                uniques.append(val)
    return uniques



if __name__ == '__main__':
    import sys
    main(sys.argv)
    
