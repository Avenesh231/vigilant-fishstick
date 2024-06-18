def dynamic_programming_example():
    # Define the problem
    n = 5
    m = 3
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1:
                dp[i][j] = j
            elif j == 1:
                dp[i][j] = i
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    # Print the dp table
    for row in dp:
        print(row)

    # Print the minimum number of operations
    print("Minimum number of operations:", dp[n][m])

dynamic_programming_example()
