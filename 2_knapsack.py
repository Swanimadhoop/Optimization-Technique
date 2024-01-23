def find_max_fit(weights, values, capacity, items):
    matrix = [[0 for _ in range(capacity + 1)] for _ in range(items + 1)]

    for i in range(1, items + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], values[i - 1] + matrix[i - 1][j - weights[i - 1]])

    print("Max weight with max profit that can be selected:", matrix[items][capacity])

    selected_coins = []
    selected_count = 0
    i, j = items, capacity

    while i > 0 and j > 0:
        if matrix[i][j] != matrix[i - 1][j]:
            selected_coins.append(i - 1)
            j -= weights[i - 1]
            i -= 1
        else:
            i -= 1

    print("Selected weights:", end=" ")
    for k in range(len(selected_coins) - 1, -1, -1):
        print(selected_coins[k] + 1, end=" ")
    print()


def main():
    items = int(input("Enter the number of items: "))
    weights = [int(x) for x in input("Enter the weights of the items: ").split()]
    values = [int(x) for x in input("Enter the values of the items: ").split()]
    capacity = int(input("Enter the capacity: "))

    find_max_fit(weights, values, capacity, items)


if __name__ == "__main__":
    main()




#output
#Enter the number of items: 4
#Enter the weights of the items: 2 3 4 2
#Enter the values of the items: 3 4 5 7
#Enter the capacity: 9
#Max weight with max profit that can be selected: 16
#Selected weights: 2 3 4 