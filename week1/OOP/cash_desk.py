class CashDesk:

    def __init__(self):
        self.money = {
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            2: 0,
            1: 0
        }

    def take_money(self, money):
        for m in money:
            self.money[m] += money[m]

    def total(self):
        total_money = 0
        for m in self.money:
            total_money += int(m)*self.money[m]
        return total_money

    def print_cash_desk(self):
        print(self.money)

    def can_withdraw_money(self, amount_of_money):

    # DO IT LATER

"""
def main():

    my_cash_desk = CashDesk()
    #Creates CashDesk instance
    my_cash_desk.print_cash_desk()
    my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
    #Add money in CashDesk
    my_cash_desk.print_cash_desk()
    print(my_cash_desk.total())

if __name__ == "__main__":
    main()
"""