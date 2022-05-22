def binary_search(list, target):
    first = 0
    last = len(list) - 1
    print("whats in list?: ", list)

    while first <= last:
        # "//" floor division operator, it rounds to nearest whole number
        midpoint = (first * last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None
