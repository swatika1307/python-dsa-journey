def print_one_to_n_backtrack(i, n):
    if(i < 1):
        return
    print_one_to_n_backtrack(i - 1, n)
    print(i)

number = int(input("Enter the number till whcih you want the series to be printed: "))
print_one_to_n_backtrack(number, number)