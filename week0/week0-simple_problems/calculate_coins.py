def calculate_coins(money):
    money *= 100
    coins = [100, 50, 20, 10, 5, 2, 1]
    answer = {}

    for coin in coins:
        neededCoins = int(money / coin)
        answer[coin] = neededCoins
        money -= coin * neededCoins

    return answer


# main
def main():
    print(calculate_coins(0.53))
    print(calculate_coins(8.94))


# PROGRAM RUN
if __name__ == '__main__':
    main()
