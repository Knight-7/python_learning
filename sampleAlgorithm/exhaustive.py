def calculate_fish():
    fish = 1
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) / 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 1


def calculate_fish2():
    fish = 1
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if total % 4 == 0:
                total = total // 4 * 5 + 1
            else:
                enough = False
                break
        if enough:
            print(total)
            break
        fish += 1


if __name__ == '__main__':
    calculate_fish()
    calculate_fish2()