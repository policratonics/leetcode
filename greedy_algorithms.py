def coin_change(coins, amount):
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            coin_count += 1
    return coin_count if amount == 0 else -1


if __name__ == '__main__':
    result = coin_change(coins=[1, 5, 10, 25], amount=67)
    print(result)
