def recursive(curr, total):
    if (curr > total):
        return

    print(f"Day {curr}")

    recursive(curr + 1, total)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursive(1, days)
    print("Harvest time!")
