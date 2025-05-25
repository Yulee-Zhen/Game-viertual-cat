class User:
    def __init__(self, name):
        self.name = name
        self.amount = 100
        self.credit = 5


    def __str__(self) -> str:
        return '-' * 17 + '\n'\
        + f'{self.name}'.center(17) + '\n'\
        + '-' * 17 + '\n'\
        + ' 💰 ' + 'Amount'.ljust(6) + ': ' + f'${self.amount}'+ '\n'\
        + ' ⭐️' + 'Credit'.ljust(6) + ': ' + f' {self.credit}' + '\n'\
        + '-' * 17
            


if __name__ == '__main__':
    user = User('Yulee')
    print(user)


