# other_nice_figures.py

def other_nice_figures(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)  # (n-i) means Total number of rows in the pattern minus the current row number
        stars = "*" * i         # The number of stars is equal to the row number
        print(spaces + stars)   # Combine spaces and stars


n = int(input("Enter n: "))  # Get user input
other_nice_figures(n)  # Call the function
