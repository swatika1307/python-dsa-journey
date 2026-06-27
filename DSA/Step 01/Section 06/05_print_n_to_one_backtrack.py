def print_n_to_one_backtrack(i, n):
    if(i > n):
        return
    print_n_to_one_backtrack(i + 1, n)
    print(i)

number = int(input("Enter the number till which you want the series to be printed: "))
i = 1
print_n_to_one_backtrack(i, number)