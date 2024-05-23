#multilevel inheritence

class Swift:
    wheels = 4

    def __init__(self) -> None:
        self.owner_name = input()

    def show_features(self):
        print('Swift has Good features')


